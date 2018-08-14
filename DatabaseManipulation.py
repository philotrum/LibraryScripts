# -*- coding: utf-8 -*
"""
Created 20140529

@author: G. Kettlewell

Plot sensor data for Sandpit noise tests
"""
import sqlite3 as lite
#import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
from scipy import stats

def NumTables(inDatabaseName):
    """ Check how many tables there are in a database """

    # Check how many tables there is in the database to determine which database version is being used
    selectSTR = 'SELECT name from sqlite_master WHERE type=\'table\''
    con = lite.connect(inDatabaseName)
    cur = con.cursor()
    cur.execute(selectSTR)
    tableNames = cur.fetchall()
    print(tableNames)
    return len(tableNames)


def ReadDatabase(inDatabaseName, inSelectSTR):
    """ Open a database, and read in all rows according to the selection criteria.
        Return the data that has been read in. """

    con = lite.connect(inDatabaseName)
    cur = con.cursor()
    cur.execute(inSelectSTR)
    rows = cur.fetchall()
    return rows

def ConvertToDateTime(inData, inIndex):
    """ Convert a tuple list to a dateTime list. """

    dates = []
    for row in inData:
        trimmedTime = str(row[inIndex]).split('.')
        dates.append(dt.datetime.strptime(str(trimmedTime[0]), '%Y-%m-%d %H:%M:%S'))
    return dates

def CalculateDeltaTime(inDates, inDates2 = None):
    """ Calculate the time between spectrum collections. """

    deltaTime = []
    if (inDates2 is None):
        # Calculate the time between elements in the list of dates passed in
        i = 1
        for row in inDates:
            if i < len(inDates):
                tmpDeltaTime = inDates[i] - inDates[i-1]
                deltaTime.append(tmpDeltaTime.total_seconds())
                i = i + 1
    else:
        # Calculate the difference between the times in the rows of the lists passed in
        i = 0
        for row in inDates:
            tmpDeltaTime = inDates[i] - inDates2[i]
            deltaTime.append(tmpDeltaTime.total_seconds())
            i = i + 1

    return deltaTime

def LoadData(inData, index):
    """ Load a column of data from the tuple data set from a databes into a list.
        You need to pass in the index of the column, 0 based.
        Returns a list with column of a data in it. """

    data = []
    for row in inData:
        data.append(row[index])
    return data

def RunningMeanFast(x, N):
    """ Calulate the running mean of x using an averaging period of N.
        returns the running mean as an nparray. """

    rm = np.convolve(x, np.ones((N,))/N)[(N-1):]
    return rm[:len(rm)-N-1]

def CalculateNoise(inData, inAveragingPeriod):
    """ Calcualtes the noise in a data set by subtracting the running mean from the
        original data set. The running mean is calulated using an averaging period of N
        samples. """

    runningMean = RunningMeanFast(inData, inAveragingPeriod)
    noise = inData[1:len(runningMean)+1] - runningMean
    noise = noise[:(len(noise) - inAveragingPeriod/2)]
    return noise

def CalculateDelta(inData):
    """ Calculate the delta between each point in a data series.
        The data must be in an array like structure. """

    deltas = []
    i = 1
    for row in inData:
        if i < len(inData):
            tmpDelta = float(inData[i]) - float(inData[i-1])
            deltas.append(tmpDelta)
            i = i + 1
    return deltas

def rsquared(x, y):
    """ Return R^2 where x and y are array-like."""

    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return r_value**2
