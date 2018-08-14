#!user/bin/env python

import ephem as eph
import time as t
from datetime import timedelta
from math import sin, radians

class SZA_Calc:
    
    def __init__(self, inLat, inLong, inEle, inTimezone=0):
        
        # Instantiate the ephem object to allow sza calculations for the sun.
        self._mObs = eph.Observer()
        self._mObs.lon = str(inLong)
        self._mObs.lat = str(inLat)
        self._mObs.elevation = inEle
        self._mTimezone = inTimezone
    
    def getSZA(self, inDateTime = None):
    
        if (inDateTime == None):
            timeStr = t.strftime('%Y/%m/%d %H:%M:%S', t.gmtime())  
        else:
            timeStr = inDateTime - timedelta(hours=self._mTimezone)
        
        self._mObs.date = timeStr
        sun = eph.Sun()
        # Call this to set the ephem object up correclty
        # t=for the current time
        sun.compute(self._mObs)
        alt = self._parse_dms(sun.alt)
        sza = 90 - alt
        
        return sza
        
    def getAlt(self, inDateTime = None):
        
        if (inDateTime == None):
            timeStr = t.strftime('%Y/%m/%d %H:%M:%S', t.gmtime())  
        else:
            timeStr = inDateTime
        
        self._mObs.date = timeStr
        sun = eph.Sun()
        # Call this to set the ephem object up correclty
        # t=for the current time
        sun.compute(self._mObs)
        alt = self._parse_dms(sun.alt)
        
        return alt
        
    def getSolarRad(self, inDateTime = None):
                   
        return sin(radians(self.getAlt(inDateTime))) * 1177.8 - 97.753
            
        
    def _dms2dd(self, degrees, minutes, seconds):
        
        dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
        
        return dd;
        
    def _parse_dms(self, dms):
        
        strDMS = str(dms)
        parts = strDMS.split(':')
        lat = self._dms2dd(parts[0], parts[1], parts[2])
        
        return (lat)
