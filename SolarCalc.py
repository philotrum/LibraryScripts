#!user/bin/env python

from astral import LocationInfo, Observer
from astral.sun import sun, sunrise, sunset, zenith, elevation
import datetime as dt
from math import sin, radians
import logging
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError

class Solar_Calc:
    
    def __init__(self, inLocName: str='', inCountryName:str='', inTimezone_tz:str='',
                    inLat:float=0.0, inLong:float=0.0, 
                    inEle:float=0.0, inTZ:float=0.0):
        '''
        This class calculates solar zenith angle, solar altitude, solar
        radiation and sunrise and sunset for the location passed in.
        
        Arguments for the overloaded constructor:

            inLocName:      The name of the location. This can be a
                            a location in the list of locations provided
                            in Astral, or it can be a new location not in
                            the list.
            inTimezone_tz:  The timezone of the location. This must be 
                            in the format recognised by timezone objects as
                            provided by pytz.  
            inCountryName:  The name of the county the location. Again, it
                            can be from the list of locations provided in
                            Astral, or it can be a new location not listed.
            inLat:          Latitude of the location. If the location is in
                            the list of locations in Astral this argument 
                            can be omitted.
            inLong:         Longitude of the location. If the location is in
                            the list of locations in Astral this argument 
                            can be omitted.
            inEle:          Elevation of the location in metres. If the location
                            is in the list of locations in Astral this argument 
                            can be omitted.
            inTZ:           Timezone offest in hours       
        '''

         # Set up logger
        self._mLogger = logging.getLogger(__name__)
        self._mLogger.debug('Entering __init__')

        # Initialise memeber variables
        self._mLon = inLong
        self._mLat = inLat
        self._mEle = inEle
        try:
            self._mTimezone = timezone(inTimezone_tz)
        except UnknownTimeZoneError:
            self._mLogger.error('Unknown timezone_tz value in the configuration file')
                
        # Set the location
        self._mCity = LocationInfo(name=inLocName, region=inCountryName, timezone=inTimezone_tz, latitude=inLat, longitude=inLong)
        self._mObserver = Observer(latitude=self._mLat, longitude=self._mLon, elevation=self._mEle)
            
    def getSZA(self, inDateTime = None):

        if (inDateTime == None):
            datetime = dt.datetime.now(self._mTimezone)  
        else:
            datetime = inDateTime

        try:
            sza = zenith(observer=self._mCity.observer)
            self._mLogger.debug('Retrieved SZA')
        except:
            self._mLogger.error('Failed to retrieve SZA from the Astral package')

        return sza
        
    def getAlt(self, inDateTime = None):
        
        if (inDateTime == None):
            datetime = dt.datetime.now(self._mTimezone)
        else:
            datetime = inDateTime
        
        try:
            altitude = elevation(observer=self._mObserver, dateandtime=datetime)
            self._mLogger.debug('Retrieved solar elevation.')
        except:
            self._mLogger.error('Failed to retrieve solar elevation from the Astral package')

        return altitude
        
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

        try:
            sunriseLocal = sunrise(observer=self._mObserver, date=datetime, tzinfo=self._mCity.timezone)
            self._mLogger.debug('Sunrise: ' + sunriseLocal.strftime('%H:%M:%S'))
        except:
            self._mLogger.error('Failed to retrieve sunrise time from Astral')
        try:
            sunsetLocal = sunset(observer=self._mObserver, date=datetime, tzinfo=self._mCity.timezone)
            self._mLogger.debug('Sunset: ' + sunsetLocal.strftime('%H:%M:%S'))
        except:
            self._mLogger.error('Failed to retrieve sunset time from Astral')

        return sunriseLocal, sunsetLocal
