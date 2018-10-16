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
        # Call this to set the ephem object up correctly
        # t=for the current time
        sun.compute(self._mObs)
        alt = self._parse_dms(sun.alt)
        
        return alt
        
    def getSolarRad(self, inDateTime = None):
                   
        if (inDateTime == None):
            dateTimeStr = t.strftime('%Y/%m/%d %H:%M:%S', t.gmtime())
        else:
            dateTimeStr = inDateTime
        
        return sin(radians(self.getAlt(dateTimeStr))) * 1177.8 - 97.753

    def getSunRiseSet(self, inDate = None):
        ''' 
        Returns the sunrise and sunset times in local time.
        Arguements:
            inDate: UTC date for which sunrise/sunset times are required. 
                    If None then returns times for today.
        '''

        if (inDate == None):
            dateStr = t.strftime('%Y/%m/%d', t.gmtime())

        utcSunrise = self._mObs.previous_rising(eph.Sun(), dateStr).datetime()
        utcSunset = self._mObs.next_setting(eph.Sun(), dateStr).datetime()

        localSunrise = utcSunrise + timedelta(hours=self._mTimezone)
        localSunset = utcSunset + timedelta(hours=self._mTimezone)

        localSunriseStr = localSunrise.strftime('%H:%M:%S')
        localSunsetStr = localSunset.strftime('%H:%M:%S')

        return localSunriseStr, localSunsetStr
            
        
    def _dms2dd(self, degrees, minutes, seconds):
        
        dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
        
        return dd
        
    def _parse_dms(self, dms):
        
        strDMS = str(dms)
        parts = strDMS.split(':')
        lat = self._dms2dd(parts[0], parts[1], parts[2])
        
        return (lat)
