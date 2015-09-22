# -*- coding: utf-8 -*
"""
Created 20140520

@author: G. Kettlewell

Stats manipulation
"""

import numpy as np
import datetime as dt

def binAndAverage(inData, inDates, inAveragingPeriod, inStartTime):

    bins = []
    dates = []
    averages = []
    tmpBin = []

    startDateTime = inStartTime
    i = 0
    while (i < len(inData)):
        binEndTime = startDateTime + dt.timedelta(minutes = inAveragingPeriod)
        if (inDates[i] < binEndTime):
            tmpBin.append(inData[i])
            i = i + 1
        else:
            dates.append(startDateTime)
            bins.append(tmpBin)
            startDateTime = binEndTime
            tmpBin = []

    for val in bins:
        averages.append(np.mean(val))

    return (dates, averages)
