"""
Convert CFS files to NWB v2 files. Adapted from the CFSConverter.py from the X_to_nwb package from Thomas Braun and Allen institute.

This script is subject to the same LICENSE as the original script.

==========================================================================
Allen Institute Software License - This software license is the 2-clause BSD license
plus a third clause that prohibits redistribution for commercial purposes without further permission.

Copyright (c) 2018. Allen Institute. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the
following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
following disclaimer in the documentation and/or other materials provided with the distribution.

3. Redistributions for commercial purposes are not permitted without the Allen Institute's written permission.
For purposes of this license, commercial purposes is the incorporation of the Allen Institute's software into
anything for which you will charge fees or other compensation. Contact terms@alleninstitute.org for commercial
licensing opportunities.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
================================================================================================

"""

from hashlib import sha256
import json
import re
import os
import glob
import warnings
import logging

from datetime import datetime
from dateutil.tz import tzlocal

import numpy as np

import pyCEDFS

from pynwb.device import Device
from pynwb import NWBHDF5IO, NWBFile
from pynwb.icephys import IntracellularElectrode

from x_to_nwb.conversion_utils import (
    PLACEHOLDER,
    V_CLAMP_MODE,
    I_CLAMP_MODE,
    I0_CLAMP_MODE,
    parseUnit,
    getStimulusSeriesClass,
    getAcquiredSeriesClass,
    createSeriesName,
    convertDataset,
    getPackageInfo,
    createCycleID,
)

log = logging.getLogger(__name__)


class CFSConverter:

    protocolStorageDir = None

    def __init__(
        self,
        inFileOrFolder,
        outFile,
        compression=True,
        globalSettingsFile=None,
        searchSettingsFile=True,
        includeChannelList=None,
        discardChannelList=None,
    ):
        """
        Convert the given cfs file to NWB. By default all ADC channel are written in to the NWB file.

        Keyword arguments:
        inFileOrFolder        -- input file, or folder with multiple files, in cfs v2 format
        outFile               -- target filepath (must not exist)
        compression           -- Toggle compression for HDF5 datasets
        searchSettingsFile    -- Search the JSON settings file and warn if it could not be found
        includeChannelList    -- ADC channels to write into the NWB file
        discardChannelList    -- ADC channels to not write into the NWB file
        """

        inFiles = []

        if os.path.isfile(inFileOrFolder):
            inFiles.append(inFileOrFolder)
        elif os.path.isdir(inFileOrFolder):
            inFiles = glob.glob(os.path.join(inFileOrFolder, "*.cfs"))
        else:
            raise ValueError(f"{inFileOrFolder} is neither a folder nor a path.")

        if includeChannelList is not None and discardChannelList is not None:
            raise ValueError("includeChannelList and discardChannelList are mutually exclusive. Pass only one of them.")
        elif includeChannelList is None and discardChannelList is None:
            includeChannelList = list("*")

        self.includeChannelList = includeChannelList
        self.discardChannelList = discardChannelList

        self.compression = compression
        self.globalSettingsFile = globalSettingsFile
        self.searchSettingsFile = searchSettingsFile

        self._settings = self._getJSONFiles(inFileOrFolder)

        self.cfss = []

        for inFile in inFiles:
            cfs = pyCEDFS.CFS(inFile)
            self.cfss.append(cfs)

            # ensure that the input file matches our expectations
            self._check(cfs)

        self.refcfs = self._getOldestcfs()
        #Disable Checks for now Trust that the user wont break it
        #self._checkAll()

        self.totalSeriesCount = self._getMaxTimeSeriesCount()

        nwbFile = self._createFile()

        device = self._createDevice()
        nwbFile.add_device(device)

        electrodes = self._createElectrodes(device)
        nwbFile.add_icephys_electrode(electrodes)

        for i in self._createStimulusSeries(electrodes):
            nwbFile.add_stimulus(i)

        for i in self._createAcquiredSeries(electrodes):
            nwbFile.add_acquisition(i)

        with NWBHDF5IO(outFile, "w") as io:
            io.write(nwbFile, cache_spec=True)

    @staticmethod
    def outputMetadata(inFile):
        if not os.path.isfile(inFile):
            raise ValueError(f"The file {inFile} does not exist.")

        root, ext = os.path.splitext(inFile)

        cfs = pyCEDFS.cfs(inFile)
        pyCEDFS.cfsHeaderDisplay.cfsInfoPage(cfs).generateHTML(saveAs=root + ".html")

    @staticmethod
    def _getProtocolName(protocolName, _json_settings):
        """
        Return the protocol/stimset name without the channel suffix.
        If the user supplies a protocol name for this file we override the file description.
        """
        proto_str = ['protocol', 'Protocol']
        keys = list(_json_settings.keys())
        proto_bool = np.isin(proto_str, keys)
        if np.any(proto_bool):
            protocolName = _json_settings[proto_str[np.nonzero(proto_bool)[0][0]]] #Grab the first instance of protocol
        return re.sub(r"_IN\d+$", "", protocolName)

    def _getJSONFiles(self, inFileOrFolder):
        """
        Search the JSON files with all miscellaneous settings.
        If `inFileOrFolder` is a folder we need one JSON file in that folder or
        multiple JSON files with the same basename as the cfs files.
        If `inFileOrFolder` is a file the JSON file must have the same
        basename.

        Returns a dict with the cfs file/folder name as key and a dictinonary with
        the settings as value.
        """

        if not self.searchSettingsFile:
            return None

        d = {}

        def loadJSON(filename):
            log.debug(f"Using JSON settings file {filename}.")
            with open(filename) as fh:
                return json.load(fh)

        def addDictEntry(d, filename):
            base, _ = os.path.splitext(filename)
            settings = base + ".json"

            if os.path.isfile(settings):
                d[filename] = loadJSON(settings)
                return None

            warnings.warn(f"Could not find the JSON file {settings} with settings.")

        if self.globalSettingsFile is not None:
            log.debug("Loading global settings file")
            self.globalSettingsDict = loadJSON(self.globalSettingsFile)

        if os.path.isfile(inFileOrFolder):
            log.debug("Searching JSON files for file conversion.")
            addDictEntry(d, inFileOrFolder)
            return d

        if os.path.isdir(inFileOrFolder):
            files = glob.glob(os.path.join(inFileOrFolder, "*.json"))

            numFiles = len(files)

            log.debug(f"Found {numFiles} JSON files for folder conversion.")

            if numFiles == 0:
                warnings.warn("Could not find any JSON file with settings.")
                return d
            elif numFiles == 1:
                # compatibility with old datasets with only one JSON file per folder
                if files[0] == self.globalSettingsFile:
                    self.globalSettingsDict = loadJSON(files[0])
                    d[inFileOrFolder] = loadJSON(files[0])
                else:
                    d[inFileOrFolder] = loadJSON(files[0])


                return d

            # iterate over all cfs files
            files = glob.glob(os.path.join(inFileOrFolder, "*.cfs"))
            for f in files:
                addDictEntry(d, f)

            return d

    def _check(self, cfs):
        """
        Check that all prerequisites are met.
        """

        
        if not (cfs.sweepPointCount > 0):
            raise ValueError("The number of data points is not larger than zero.")
        elif not (cfs.sweepCount > 0):
            raise ValueError("Found no sweeps.")
        elif not (cfs.channelCount > 0):
            raise ValueError("Found no channels.")
        elif cfs.channelCount != len(cfs.channelList):
            raise ValueError("Internal channel count is inconsistent.")
        elif cfs.sweepCount != len(cfs.sweepList):
            raise ValueError("Internal sweep count is inconsistent.")

        _json_settings, jsonSource = self._findSettingsEntry(cfs)
        if _json_settings is not None:
            channels = _json_settings['Resp Channels']
        else:
            channels = range(cfs.channelCount)

        for sweep in range(cfs.sweepCount):
            for channel in channels:
                cfs.setSweep(sweep, channel=channel)

                if cfs.sweepUnitsX != "sec":
                    raise ValueError(f"Unexpected x units of {cfs.sweepUnitsX}.")

                if np.isnan(cfs.sweepC).any():
                    raise ValueError(
                        f"Found at least one 'Not a Number' "
                        f"entry in stimulus channel {channel} of sweep {sweep} "
                        f"in file {cfs.cfsFilePath} using protocol {cfs.protocol}."
                    )

    def _reduceChannelList(self, cfs, _json_settings):
        """
        Return a reduced channel list taking into account the include and discard ADC channel settings.
        """
        full_list = _json_settings['Resp Channels']
        if self.includeChannelList is not None:

            if self.includeChannelList == list("*"):
                return full_list

            return list(set(full_list).intersection(self.includeChannelList))

        elif self.discardChannelList is not None:
            return list(set(full_list) - set(full_list).intersection(self.discardChannelList))

        raise ValueError("Unexpected include and discard channel settings.")

    def _checkAll(self):
        """
        Check that all loaded cfs files have a minimum list of properties in common.

        These are:
        - Digitizer device
        - Telegraph device
        - Creator Name
        - Creator Version
        - cfsVersion
        - channelList
        """

        for cfs in self.cfss:
            source = f"({self.refcfs.cfsFilePath} vs {cfs.cfsFilePath})"
            refChannelList = self._reduceChannelList(self.refcfs)
            channelList = self._reduceChannelList(cfs)
            if refChannelList != channelList:
                raise ValueError(f"channelList ({refChannelList} vs {channelList} does not match in {source}.")

    def _getOldestcfs(self):
        """
        Return the cfs file with the oldest starting time stamp.
        """

        def getTimestamp(cfs):
            return cfs.cfsDateTime

        return min(self.cfss, key=getTimestamp)

    def _getClampMode(self, cfs, channel, str_mode=''):
        """
        Return the clamp mode of the given channel.
        """
        cmode = None
        if str_mode == 'IC':
            cmode = I_CLAMP_MODE
        elif str_mode == 'VC':
            cmode = V_CLAMP_MODE
        return cmode

    def _getMaxTimeSeriesCount(self):
        """
        Return the maximum number of TimeSeries which will be created from all cfs files.
        """

        def getCount(cfs):
            return cfs.sweepCount * cfs.channelCount

        return sum(map(getCount, self.cfss))

    def _createFile(self):
        """
        Create a pynwb NWBFile object from the cfs file contents.
        """

        def formatVersion(version):
            return f"{version['major']}.{version['minor']}.{version['bugfix']}.{version['build']}"

        def getFileComments(cfss):
            """
            Return the file comments of all files. Returns an empty string if none are present.
            """

            comments = {}

            for cfs in cfss:
                if len(cfs.cfsFileComment) > 0:
                    comments[os.path.basename(cfs.cfsFilePath)] = cfs.cfsFileComment

            if not len(comments):
                return ""

            return json.dumps(comments)

        session_description = getFileComments(self.cfss)
        if len(session_description) == 0:
            session_description = PLACEHOLDER

        identifier = sha256(" ".join([cfs.fileGUID for cfs in self.cfss]).encode()).hexdigest()
        session_start_time = datetime.combine(
            self.refcfs.cfsDateTime.date(), self.refcfs.cfsDateTime.time(), tzinfo=tzlocal()
        )
        creatorName = " "
        creatorVersion = " "
        experiment_description = f" "
        source_script_file_name = "conversion.py"
        source_script = json.dumps(getPackageInfo(), sort_keys=True, indent=4)
        session_id = PLACEHOLDER

        return NWBFile(
            session_description=session_description,
            identifier=identifier,
            session_start_time=session_start_time,
            experimenter=None,
            experiment_description=experiment_description,
            session_id=session_id,
            source_script_file_name=source_script_file_name,
            source_script=source_script,
        )

    def _createDevice(self):
        """
        Create a pynwb Device object from the cfs file contents.
        """

        digitizer = self.refcfs.fileVars[0]['desc']
        telegraph = self.refcfs.fileVars[0]['desc']

        return Device(f"{digitizer} with {telegraph}")

    def _createElectrodes(self, device):
        """
        Create pynwb ic_electrodes objects from the cfs file contents.
        """

        return [
            IntracellularElectrode(f"Electrode {x:d}", device, description=PLACEHOLDER) for x in self.refcfs.channelList
        ]

    def _calculateStartingTime(self, cfs):
        """
        Calculate the starting time of the current sweep of `cfs` relative to the reference cfs file.
        """

        delta = cfs.cfsDateTime - self.refcfs.cfsDateTime

        return delta.total_seconds() + cfs.sweepX[0]

    def _createStimulusSeries(self, electrodes):
        """
        Return a list of pynwb stimulus series objects created from the cfs file contents.
        """

        series = []
        counter = 0

        for file_index, cfs in enumerate(self.cfss):

            _json_settings, jsonSource = self._findSettingsEntry(cfs)
            log.debug(f"Using JSON settings for {jsonSource}.")


            stimulus_description = CFSConverter._getProtocolName(cfs.protocol, _json_settings)
            scale_factor = self._getScaleFactor(cfs, stimulus_description)

            for sweep in range(cfs.sweepCount):
                cycle_id = int(createCycleID([file_index, sweep], total=self.totalSeriesCount))
                for channel in _json_settings['Stim Channels']:

                    cfs.setSweep(sweep, channel=channel, absoluteTime=True)
                    name, counter = createSeriesName("index", counter, total=self.totalSeriesCount)
                    data = convertDataset(cfs.sweepC * scale_factor, self.compression)
                    conversion, _ = parseUnit(cfs.sweepUnitsC)
                    electrode = electrodes[channel]
                    gain = np.nan #cfs._dacSection.fDACScaleFactor[channel]
                    resolution = np.nan
                    starting_time = self._calculateStartingTime(cfs)
                    rate = float(cfs.dataRate)
                    description = json.dumps(
                        {
                            "cycle_id": cycle_id,
                            "protocol": stimulus_description,
                            "protocolPath": cfs.protocolPath,
                            "file": os.path.basename(cfs.cfsFilePath),
                            "name": cfs.chVars[channel]['Channel Name'],
                            "number": int(cfs.chVars[channel]['Channel']),
                        },
                        sort_keys=True,
                        indent=4,
                    )

                    seriesClass = getStimulusSeriesClass(self._getClampMode(cfs, channel, str_mode=_json_settings['Clamp Mode']))

                    if seriesClass is not None:
                        stimulus = seriesClass(
                            name=name,
                            data=data,
                            sweep_number=np.uint64(cycle_id),
                            electrode=electrode,
                            gain=gain,
                            resolution=resolution,
                            conversion=conversion,
                            starting_time=starting_time,
                            rate=rate,
                            description=description,
                            stimulus_description=stimulus_description,
                        )

                        series.append(stimulus)

        return series

    def _findSettingsEntry(self, cfs):
        """
        Return the settings dictionary for the given cfs file, either the file
        specific, or the global one for the folder, or None as first tuple element.
        The second element is the source of the data.
        """

        if self._settings is None or not self.searchSettingsFile:
            return None, None

        filename = cfs.cfsFilePath

        if self.globalSettingsFile is not None:
            return self.globalSettingsDict, filename


        try:
            return self._settings[filename], filename
        except KeyError:
            dirname = os.path.dirname(filename)

            try:
                return self._settings[dirname], dirname
            except KeyError:
                return None, None

    def _getScaleFactor(self, cfs, stimset):
        """
        Return the stimulus scale factor for the stimset of the cfs file.
        """

        DEFAULT_SCALE_FACTOR = 1.0

        if not self.searchSettingsFile:
            return DEFAULT_SCALE_FACTOR

        try:
            settings, _ = self._findSettingsEntry(cfs)
            return float(settings["ScaleFactors"][stimset])
        except (TypeError, KeyError):
            warnings.warn(
                f"Could not find the scale factor for the stimset {stimset}, using {DEFAULT_SCALE_FACTOR} as fallback."
            )
            return DEFAULT_SCALE_FACTOR

    def _getAmplifierSettings(self, cfs, clampMode, adcName):
        """
        Return a dict with the amplifier settings read out form the JSON file.
        Unset values are returned as `NaN`.
        """

        d = {}
        settings = None

        if self.searchSettingsFile:
            try:
                # JSON stores adcName without spaces

                amplifier = "unknown"
                cfsSettings, _ = self._findSettingsEntry(cfs)
                adcNameWOSpace = adcName.replace(" ", "")
                amplifier = cfsSettings["uids"][adcNameWOSpace]
                settings = cfsSettings[amplifier]

                if settings["GetMode"] != clampMode:
                    warnings.warn(
                        f"Stored clamp mode {settings['GetMode']} does not match requested "
                        f"clamp mode {clampMode} of channel {adcName}."
                    )
                    settings = None
            except (TypeError, KeyError):
                warnings.warn(f"Could not find settings for amplifier {amplifier} of channel {adcName}.")
                settings = None

        if settings:
            if clampMode == V_CLAMP_MODE:
                d["capacitance_slow"] = settings["GetSlowCompCap"]
                d["capacitance_fast"] = settings["GetFastCompCap"]

                if settings["GetRsCompEnable"]:
                    d["resistance_comp_correction"] = settings["GetRsCompCorrection"]
                    d["resistance_comp_bandwidth"] = settings["GetRsCompBandwidth"]
                    d["resistance_comp_prediction"] = settings["GetRsCompPrediction"]
                else:
                    d["resistance_comp_correction"] = np.nan
                    d["resistance_comp_bandwidth"] = np.nan
                    d["resistance_comp_prediction"] = np.nan

                if settings["GetWholeCellCompEnable"]:
                    d["whole_cell_capacitance_comp"] = settings["GetWholeCellCompCap"]
                    d["whole_cell_series_resistance_comp"] = settings["GetWholeCellCompResist"]
                else:
                    d["whole_cell_capacitance_comp"] = np.nan
                    d["whole_cell_series_resistance_comp"] = np.nan

            elif clampMode in (I_CLAMP_MODE, I0_CLAMP_MODE):
                if settings["GetHoldingEnable"]:
                    d["bias_current"] = settings["GetHolding"]
                else:
                    d["bias_current"] = np.nan

                if settings["GetBridgeBalEnable"]:
                    d["bridge_balance"] = settings["GetBridgeBalResist"]
                else:
                    d["bridge_balance"] = np.nan

                if settings["GetNeutralizationEnable"]:
                    d["capacitance_compensation"] = settings["GetNeutralizationCap"]
                else:
                    d["capacitance_compensation"] = np.nan
            else:
                warnings.warn("Unsupported clamp mode {clampMode}")
        else:
            if clampMode == V_CLAMP_MODE:
                d["capacitance_slow"] = np.nan
                d["capacitance_fast"] = np.nan
                d["resistance_comp_correction"] = np.nan
                d["resistance_comp_bandwidth"] = np.nan
                d["resistance_comp_prediction"] = np.nan
                d["whole_cell_capacitance_comp"] = np.nan
                d["whole_cell_series_resistance_comp"] = np.nan
            elif clampMode in (I_CLAMP_MODE, I0_CLAMP_MODE):
                d["bias_current"] = np.nan
                d["bridge_balance"] = np.nan
                d["capacitance_compensation"] = np.nan
            else:
                warnings.warn("Unsupported clamp mode {clampMode}")

        return d

    def _createAcquiredSeries(self, electrodes):
        """
        Return a list of pynwb acquisition series objects created from the cfs file contents.
        """

        series = []
        counter = 0

        for file_index, cfs in enumerate(self.cfss):

            
            _, jsonSource = self._findSettingsEntry(cfs)
            _json_settings = _
            log.debug(f"Using JSON settings for {jsonSource}.")
            stimulus_description = CFSConverter._getProtocolName(cfs.protocol, _json_settings )
            channelList = self._reduceChannelList(cfs, _json_settings)
            log.debug(f"Channel lists: original {_json_settings['Resp Channels']}, reduced {channelList}")

            if len(channelList) == 0:
                warnings.warn(
                    f"The channel settings {self.includeChannelList} (included) and {self.discardChannelList} (discarded) resulted "
                    f"in an empty channelList for {cfs.cfsFilePath} with the unfiltered channels being {_json_settings['Resp Channels']}."
                )
                continue

            for sweep in range(cfs.sweepCount):
                cycle_id = createCycleID([file_index, sweep], total=self.totalSeriesCount)

                for channel in _json_settings['Resp Channels']:

                    adcName = cfs.chVars[channel]['Channel Name']
                    adcNum = cfs.chVars[channel]['Channel']
                    if adcNum not in channelList:
                        continue

                    cfs.setSweep(sweep, channel=channel, absoluteTime=True)
                    name, counter = createSeriesName("index", counter, total=self.totalSeriesCount)
                    data = convertDataset(cfs.sweepY, self.compression)
                    conversion, _ = parseUnit(cfs.sweepUnitsY)
                    electrode = electrodes[channel]
                    gain = np.nan #cfs._adcSection.fADCProgrammableGain[channel]
                    resolution = np.nan
                    starting_time = self._calculateStartingTime(cfs)
                    rate = float(cfs.dataRate)
                    description = json.dumps(
                        {
                            "cycle_id": cycle_id,
                            "protocol": stimulus_description,
                            "protocolPath": cfs.protocolPath,
                            "file": os.path.basename(cfs.cfsFilePath),
                            "name": adcName,
                            "number": int(cfs.chVars[channel]['Channel']),
                        },
                        sort_keys=True,
                        indent=4,
                    )

                    clampMode = self._getClampMode(cfs, channel, str_mode=_json_settings['Clamp Mode'])
                    settings = self._getAmplifierSettings(cfs, clampMode, adcName)
                    seriesClass = getAcquiredSeriesClass(clampMode)

                    if clampMode == V_CLAMP_MODE:
                        acquistion_data = seriesClass(
                            name=name,
                            data=data,
                            sweep_number=np.uint64(cycle_id),
                            electrode=electrode,
                            gain=gain,
                            resolution=resolution,
                            conversion=conversion,
                            starting_time=starting_time,
                            rate=rate,
                            description=description,
                            capacitance_slow=settings["capacitance_slow"],
                            capacitance_fast=settings["capacitance_fast"],
                            resistance_comp_correction=settings["resistance_comp_correction"],
                            resistance_comp_bandwidth=settings["resistance_comp_bandwidth"],
                            resistance_comp_prediction=settings["resistance_comp_prediction"],
                            stimulus_description=stimulus_description,
                            whole_cell_capacitance_comp=settings["whole_cell_capacitance_comp"],  # noqa: E501
                            whole_cell_series_resistance_comp=settings["whole_cell_series_resistance_comp"],
                        )  # noqa: E501

                    elif clampMode in (I_CLAMP_MODE, I0_CLAMP_MODE):
                        acquistion_data = seriesClass(
                            name=name,
                            data=data,
                            sweep_number=np.uint64(cycle_id),
                            electrode=electrode,
                            gain=gain,
                            resolution=resolution,
                            conversion=conversion,
                            starting_time=starting_time,
                            rate=rate,
                            description=description,
                            bias_current=settings["bias_current"],
                            bridge_balance=settings["bridge_balance"],
                            stimulus_description=stimulus_description,
                            capacitance_compensation=settings["capacitance_compensation"],
                        )
                    else:
                        raise ValueError(f"Unsupported clamp mode {clampMode}.")

                    series.append(acquistion_data)

        return series
