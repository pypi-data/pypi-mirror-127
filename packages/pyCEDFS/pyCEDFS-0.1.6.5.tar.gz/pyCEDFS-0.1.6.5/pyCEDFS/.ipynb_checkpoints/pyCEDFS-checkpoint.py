
import os
import sys
import glob
import time
import datetime
import numpy as np
from pathlib import PureWindowsPath
import hashlib
import ctypes
import matplotlib.pyplot as plt
import pkg_resources

# Load the shared library into c types.
dll_path = pkg_resources.resource_filename(__name__,"CFS64c.dll")

CFS64 = ctypes.CDLL(dll_path)
import logging
logging.basicConfig(level=logging.WARN)
log = logging.getLogger(__name__)

dataVarTypes = [('INT1', ctypes.c_int), ('WRD1', ctypes.c_ushort),('INT2', ctypes.c_int16),('WRD2', ctypes.c_ushort),('INT4', ctypes.c_int32), ('RL4', ctypes.c_longdouble), ('RL8', ctypes.c_longdouble), ( 'LSTR', ctypes.create_string_buffer)]
#define INT1    0                            
#define WRD1    1
#define INT2    2
#define WRD2    3
#define INT4    4
#define RL4     5
#define RL8     6
#define LSTR    7

class CFS(object):
    """
    
    """

    def __init__(self, cfsFilePath):

        self.cfsFilePath = os.path.abspath(cfsFilePath)
        self.cfsFolderPath = os.path.dirname(self.cfsFilePath)


        if not os.path.exists(self.cfsFilePath):
            raise ValueError("CFS file does not exist: %s" % self.cfsFilePath)
        self.CFSID = os.path.splitext(os.path.basename(self.cfsFilePath))[0]
        
        ##Open the file and pass the handle ##
        open = CFS64.OpenCFSFile
        open.restype = ctypes.c_short
        C_file = ctypes.create_string_buffer(self.cfsFilePath.encode())
        handle = open(C_file, 0, 0)
        self._fileHandle = handle
        log.debug(f"Loaded file: {self.CFSID} with handle: {self._fileHandle}")
        ## Load the File properties and pass them to class ##
        _filedate = ctypes.create_string_buffer(10)  
        _filetime = ctypes.create_string_buffer(10)  
        _comment = ctypes.create_string_buffer(256)
        CFS64.GetGenInfo(self._fileHandle, _filedate, _filetime, _comment)
        self.fileDate = _filedate.value.decode()
        self.fileTime = _filetime.value.decode()
        self.fileComment = _comment.value.decode()   
        _channels = ctypes.c_short(14)
        _dsvars = ctypes.c_short(14)
        _fvars = ctypes.c_short(14)
        _ds = ctypes.c_ushort(14)
        test = CFS64.GetFileInfo(self._fileHandle, ctypes.byref(_channels),ctypes.byref(_dsvars), ctypes.byref(_fvars), ctypes.byref(_ds))
        
        self.channels = _channels.value
        self.channelList = np.arange(1, _channels.value)
        self.datasetVarsCount = _dsvars.value
        self.fileVarsCount = _fvars.value
        self.datasets = _ds.value
        self.datasetList = np.arange(1, _ds.value+2) ##Datasets start at 1?
        ## Load the vars from each functions ##
        self.fileVars = self._build_file_vars()
        self.dsVars = self._build_ds_vars()
        self.chVars = self._build_ch_vars()
        self.datasetChaVars = self._build_dsch_vars()
        self.sweeps = self.datasets ##Number of ds == num sweeps?
        self.sweepList = np.arange(1,_ds.value+1)


        ## Try to read sweep data ##
        self.dataX, self.dataY = self._read_data()
        #close the file?
        CFS64.CloseCFSFile(self._fileHandle)
        return
    def _build_attr_from_dict(self):



        return

    def _build_file_vars(self):
        ### Populate the Vars list
        files_vars = []
        #Create our ctypes to avoid memory hog
        _size = ctypes.c_short()
        _type = ctypes.c_short()
        _units = ctypes.create_string_buffer(20)  
        _desc = ctypes.create_string_buffer(50) 
        ###Populate file Vars
        for x in np.arange(self.fileVarsCount):
            CFS64.GetVarDesc(self._fileHandle, ##File self._fileHandle
                            ctypes.c_short(x), ##Var no
                            ctypes.c_short(0), ##File var = 0
                            ctypes.byref(_size), ctypes.byref(_type), _units, _desc)
            if _type.value != 7:
                _var = dataVarTypes[_type.value][1](99)
                _datas = ctypes.c_short()
                code = CFS64.GetVarVal(self._fileHandle,##Handle
                                     ctypes.c_short(x), ##Var no
                                    ctypes.c_short(0),ctypes.byref(_datas),ctypes.byref( _var))
                var_val = _var.value
            else:
                _var = dataVarTypes[_type.value][1](_size.value)
                _datas = ctypes.c_short()
                code = CFS64.GetVarVal(self._fileHandle, ctypes.c_short(x), ctypes.c_short(0),ctypes.byref(_datas),_var)
                var_val = _var.value.decode()
            dict = {"desc":_desc.value.decode(), "size": _size.value, "units": _units.value.decode(), "type":dataVarTypes[_type.value][0], "value": var_val}
            files_vars.append(dict)
        return files_vars

    def _build_ds_vars(self):
        ##Populate the DS Vars
        ds_vars = []
        #Create our ctypes to avoid memory hog
        _size = ctypes.c_short()
        _type = ctypes.c_short()
        _units = ctypes.create_string_buffer(20)  
        _desc = ctypes.create_string_buffer(50) 
        for d in self.datasetList:
            temp_ds_vars = []
            for x in np.arange(self.datasetVarsCount+1):
                _datas = ctypes.c_ushort(d)
                CFS64.GetVarDesc(self._fileHandle, ctypes.c_short(x), ctypes.c_short(1), ctypes.byref(_size), ctypes.byref(_type), _units, _desc)
                if _type.value != 7:
                    _var = dataVarTypes[_type.value][1]()
                    code = CFS64.GetVarVal(self._fileHandle, ctypes.c_short(x), ctypes.c_short(1),ctypes.byref(_datas),ctypes.byref(_var))
                    var_val = _var
                else:
                    _var = dataVarTypes[_type.value][1](_size.value)
                    code = CFS64.GetVarVal(self._fileHandle, ctypes.c_short(x), ctypes.c_short(1),ctypes.byref(_datas),_var)        
                    var_val = _var.value.decode()
                dict = {"desc":_desc.value.decode(), "size": _size.value, "units": _units.value.decode(), "type":dataVarTypes[_type.value][0], "value": var_val}
           
                temp_ds_vars.append(dict)
            ds_vars.append(temp_ds_vars)
        return ds_vars

    def _build_ch_vars(self):
        ### Populate Channel vars
        ch_vars = []
        _channame = ctypes.create_string_buffer(21) 
        _xunits = ctypes.create_string_buffer(20) 
        _yunits = ctypes.create_string_buffer(20)
        _kind = ctypes.c_short()
        _type = ctypes.c_short()
        _spacing = ctypes.c_short()
        _other = ctypes.c_short()
        for ch in np.arange(self.channels):
            _ch = ctypes.c_short(ch)
            CFS64.GetFileChan(self._fileHandle, _ch, _channame, _xunits, _yunits, ctypes.byref(_type), ctypes.byref(_kind), ctypes.byref(_spacing), ctypes.byref(_other))
            dict = {'Channel': ch, 'Channel Name': _channame.value.decode(), 'X Units': _xunits.value.decode(), 'Y Units': _yunits.value.decode(), 'Type': _type.value, 'Kind': _kind.value, 'Spacing': _spacing.value, 'Other': _other.value}
            ch_vars.append(dict)
        return ch_vars

    def _build_dsch_vars(self):
        dsch_vars = []
        _start = ctypes.c_long()
        _points = ctypes.c_long()
        _yscale = ctypes.c_float()
        _yoffset = ctypes.c_float()
        _xscale = ctypes.c_float()
        _xoffset = ctypes.c_float()
        for ch in np.arange(self.channels):
            ds_dict = []
            for x in np.arange(1,self.datasets+1):
                CFS64.GetDSChan(self._fileHandle, 
                               ctypes.c_short(ch), ##Channel
                               ctypes.c_ushort(x),
                               ctypes.byref(_start),
                               ctypes.byref(_points),
                               ctypes.byref(_yscale),
                               ctypes.byref(_yoffset),
                               ctypes.byref(_xscale),
                               ctypes.byref(_xoffset),
                                 )
                dict = {'Channel': ch, 'ch start': _start.value, 'points': _points.value, 'yscale': _yscale.value, 'yoffset': _yoffset.value, 'xscale': _xscale.value, 'xoffset': _xoffset.value}
                ds_dict.append(dict)
            dsch_vars.append(ds_dict)
        return dsch_vars

    def _read_data(self):
        ##try to read data
        dataX = []
        dataY = []
        chanData = CFS64.GetChanData
        
        for ch in np.arange(0, self.channels):
            ch_x =[]
            ch_y = []
            for x in np.arange(1,self.datasets +1):
                channel_p = self.datasetChaVars[ch][x-1]['points'] * 2 ##Pull the datasize. the points are multiplied by 2 to reflect the x and Y data which are stacked horizontally.
                dtype = dataVarTypes[self.chVars[ch]['Type']][1] #the datatype of the channel
                _dataarray = (dtype * channel_p)() ##Declare the array in memory for the function to return data into
                chanData.argtypes = (ctypes.c_short,ctypes.c_short,ctypes.c_ushort,ctypes.c_long,ctypes.c_short, ctypes.POINTER(dtype), ctypes.c_long)
                pointsRead = chanData(self._fileHandle, 
                                ctypes.c_short(ch), ##Channel
                                 ctypes.c_ushort(x), ##DS
                                 ctypes.c_long(0), ##first element
                                 ctypes.c_short(0), ###Number of elements to pull 0==all
                                _dataarray, ###Dump into this array
                                 ctypes.c_long(channel_p * 2))##Number of data points provided
                data = np.ctypeslib.as_array(_dataarray) #convert the data into a numpy array
                ds_y = data[:int(channel_p/2)] ##first half of the data is the Y value
                ds_x = data[int(channel_p/2):] ##second half of the data appears to be X value, however if data is EQUALSPACED this is all zeros and we generate it later. 
                
                yscale = self.datasetChaVars[ch][x-1]['yscale']
                yoffset = self.datasetChaVars[ch][x-1]['yoffset']
                xscale = self.datasetChaVars[ch][x-1]['xscale']
                xoffset = self.datasetChaVars[ch][x-1]['xoffset']
                if pointsRead > 0:
                    if dtype != ctypes.c_long:
                        ds_y = ds_y * yscale + yoffset  #data is in int format must be scaled and offset with the variables 
                    #ds_x = ds_x * xscale

                    ds_x = np.cumsum(np.hstack((xoffset,np.full(int(channel_p/2)-1,xscale))))
                

                    ch_x.append(ds_x)
               
                    ch_y.append(ds_y)
            ch_x = np.vstack(ch_x)
            ch_y = np.vstack(ch_y)
            dataX.append(ch_x)
            dataY.append(ch_y)
        
        return dataX, dataY

    def _debug_plot(self, fignum=0, figsize=(10,10)):
            
            fig, axes = plt.subplots(nrows = self.channels, num=fignum, figsize=figsize)
            for x in np.arange(self.channels):
                for a in np.arange(self.sweeps):
                    axes[x].plot(self.dataX[x][a,:], self.dataY[x][a,:], label=f"{a}")

    
            
        


