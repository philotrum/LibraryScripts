#!/user/bin/env python

# Written by G. Kettlewell in May 2017
# This is a minimal configuration file handler. I wrote this because
# the library config parser that is available is over featured for
# what I need, and imports a very large amount of unrequired code.

import os
import logging

class configFileParseCLS():
    
    def __init__(self, inConfigFileName = ''):        
        
        self._mLogger = logging.getLogger(__name__)
        
        self._mSettings = []
        self._mConfigFileName = inConfigFileName
        self._mLogger.debug('Filename: ' + self._mConfigFileName)
        if (self._mConfigFileName == ''):
            self._mFilenameSet = False
        else:
            self._mFilenameSet = True
            
        self._mFileLoaded = False

    @property
    def configFileName(self):
        
        # only needed to declare the property
        pass
    
    @configFileName.setter
    def configFileName(self, inName):
        
        self._mConfigFileName = inName
        self._mFilenameSet = True
        
    @property
    def fileExists(self):
        
        return os.path.isfile(self._mConfigFileName)
        
    @property
    def fileLoaded(self):
        
        return self._mFileLoaded
        
    def add(self, inKey, inVal):
        
        tmpSetting = _settingCLS(inKey, inVal)
        
        # Check if setting already exists. Throw assertion if it does.
        for obj in self._mSettings:
            if (obj.key == tmpSetting.key):
                self._mLogger.error('Tried to add key that already exists: ' + inKey)
                assert(False)
            
        # The key is unique, so it is ok to append it.
        self._mSettings.append(tmpSetting)
        
    def update(self, inKey, inVal):
        
        for obj in self._mSettings:
            if (inKey == obj.key):
                obj.val = inVal
                return
        
        self._mLogger.error('Tried to update non-existent key: ' + inKey)
        assert(False)
    
    def getIntVal(self, inKey):
        
        # Find the setting
        for obj in self._mSettings:
            if (inKey == obj.key):
                try:
                    return int(obj.val)
                except:
                    self._mLogger.error('Couldn\'t cast the value to an integer: Value = ' + str(obj.val))
                    assert(False)
                
        self._mLogger.error('Tried to retrieve non-existent setting: ' + inKey)
        assert(False)
                
    def getFloatVal(self, inKey):
        
        # Find the setting
        for obj in self._mSettings:
            if (inKey == obj.key):
                try:
                    return float(obj.val)
                except:
                    self._mLogger.error('Couldn\'t cast the value to a float: Value = ' + str(obj.val))
                    assert(False)
                
        self._mLogger.error('Tried to get non-existent float key: ' + inKey)
        assert False
                
    def getStringVal(self, inKey):
        
        # Find the setting
        for obj in self._mSettings:
            if (inKey == obj.key):
                return str(obj.val)
                
        self._mLogger.error('Tried to get non-existent string key: ' + inKey)
        assert(False)
                
    def getBoolVal(self, inKey):
        
        # Find the setting
        for obj in self._mSettings:
            if (inKey == obj.key):
                if (obj.val == True or obj.val == 'True'):
                    return True
                elif (obj.val == False or obj.val == 'False'):
                    return False
                else:
                    self._mLogger.error('Couln\'t cast the value to a bool: Value = ' + str(obj.val))
                    assert(False)

        self._mLogger.error('Tried to get non-existent bool key: ' + inKey)
        assert(False)
    
    def readFile(self):
        
        if (self._mFilenameSet == False):
            self._mLogger('Tried to read a config file without setting the filename.')
            assert(False)
        
        #self._mLogger.debug('Filename: ' + self._mConfigFileName)
        lines = [line.rstrip('\n') for line in open(self._mConfigFileName)]     
        for line in lines:
            tmp = line.split(',')
            tmpSetting = _settingCLS(tmp[0].strip(), tmp[1].strip())
            self._mSettings.append(tmpSetting)
            
        self._mFileLoaded = True
        
    def writeFile(self):
        
        if (self._mFilenameSet == False):
            self._mLogger('Tried to write the config file without setting the filename.')
            assert(False)
        
        outs = open(self._mConfigFileName, 'w')
        for obj in self._mSettings:
            outs.write(obj.key + ' , ' + str(obj.val) + '\n')
            
        outs.close

class _settingCLS():
    
    def __init__(self, inKey = '', inVal = None):
        
        self._mKey = inKey
        self._mVal = inVal
        
    @property
    def key(self):
        
        return self._mKey
        
    @key.setter
    def key(self, inKey):    
        
        self._mKey = inKey
        
    @property
    def val(self):
        
        return self._mVal
        
    @val.setter
    def val(self, inVal):
        
        self._mVal = inVal