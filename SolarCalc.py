#!user/bin/env python

from astral import Astral, Location
from pytz import timezone
import pytz
import datetime as dt
from math import sin, radians
import logging

class Solar_Calc:
    
    def __init__(self, inLocName: str='', inTimezone:str='', inCountyName:str='', 
                    inLat:float=0.0, inLong:float=0.0, 
                    inEle:float=0.0):
        '''
        This class calculates solar zenith angle, solar altitude, solar
        radiation and sunrise and sunset for the location passed in.
        
        Arguments for the overloaded constructor:

            inLocName:      The name of the location. This can be a
                            a location in the list of locations provided
                            in Astral, or it can be a new location not in
                            the list.
            inCountryName:  The name of the county the location. Again, it
                            can be from the list of locations provided in
                            Astral, or it can be a new location not listed.
            inLat:          Latitude of the location. If the location is in
                            the list of locations in Astral this argument 
                            can be omitted.
            inLong:         Longitude of the location. If the location is in
                            the list of locations in Astral this argument 
                            can be omitted.
            inEle:          Elevation of the loaction in metres. If the location
                            is in the list of locations in Astral this argument 
                            can be omitted.
            inTimezone:     The timezone of the location. This must be 
                            in the format recognised by timezone objects as
                            provided by pytz.         
        '''

         # Set up logger
        self._mLogger = logging.getLogger(__name__)

        # Initialise memeber variables
        self._mAstral = Astral()
        self._mAstral.solar_depression = 'civil'
        self._mLon = inLong
        self._mLat = inLat
        self._mEle = inEle
        self._mLogger.debug('Timezone_tz: ' + inTimezone)
        self._mTimezone = timezone(inTimezone)
        
        # Set the location
        try:
            self._mLocation = self._mAstral[inLocName]
        except:
            self._mLocation = Location(info=(inLocName, inCountyName, 
                                  inLat, inLong, inTimezone,
                                  inEle))
            
    def getSZA(self, inDateTime = None):

        if (inDateTime == None):
            datetime = dt.datetime.now(self._mTimezone)  
        else:
            datetime = inDateTime
    
        return self._mAstral.solar_zenith(datetime, self._mLat, self._mLon)
        
    def getAlt(self, inDateTime = None):
        
        if (inDateTime == None):
            datetime = dt.datetime.now(self._mTimezone)
        else:
            datetime = inDateTime
                
        return self._mAstral.solar_elevation(datetime, self._mLat, self._mLon )
        
    def getSolarRad(self, inDateTime = None):
                   
        if (inDateTime == None):
            datetime = dt.datetime.now(self._mTimezone)
        else:
            datetime = inDateTime

        alt = self.getAlt(datetime)
        
        return sin(radians(alt)) * 1177.8 - 97.753

    def getSunRiseSet(self, inDateTime = None):
        ''' 
        Returns the sunrise and sunset times in local time.
        Arguments:
            inDate: Local date for which sunrise/sunset times are required. 
                    If None then returns times for today.
        '''

        if (inDateTime == None):
            datetime = dt.datetime.now(self._mTimezone)
        else:
            datetime = inDateTime

        ret = self._mLocation.sun(date=datetime)

        return ret['sunrise'], ret['sunset']
