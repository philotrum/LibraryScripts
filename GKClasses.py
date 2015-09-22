# -*- coding: utf-8 -*
"""
Created 20140529

@author: G. Kettlewell
"""

class spectraDiagCLS(object):
    def __init__(self, fDate=None, fRMS=None, fSpecMax=None, fIterations=None):

        if (fDate == None):
            fDate = []
        else:
            fDate = self.fDate
        if (fRMS == None):
            fRMS = []
        else:
            fRMS = self.fRMS
        if (fSpecMax == None):
            fSpecMax = []
        else:
            fSpecMax = self.fSpecMax
        if (fIterations== None):
            fIterations = []
        else:
            fIterations = self.fIterations

class CellTempControlCLS(object) :
    def __init__(self, fDate=None,
                       fCellInSpecEnd=None,
                       fCellInBlankEnd=None,
                       fCellOutSpecEnd=None,
                       fCellOutBlankEnd=None,
                       fCellOutSpecEndNoise = None,
                       fCellOutBlankEndNoise = None,
                       fCellOutSpecEndRM = None,
                       fCellOutBlankEndRM = None,
                       fFlowIn = None,
                       fFlowOut = None):

        if (fDate == None):
            fDate = []
        else:
            fDate = self.fDate

        if (fCellInSpecEnd == None):
            fCellInSpecEnd = []
        else:
            fCellInSpecEnd = self.fCellInSpecEnd

        if (fCellInBlankEnd == None):
            fCellInBlankEnd = []
        else:
            fCellInBlankEnd = self.fCellInBlankEnd

        if (fCellOutSpecEnd== None):
            fCellOutSpecEnd = []
        else:
            fCellOutSpecEnd = self.fCellOutSpecEnd

        if (fCellOutBlankEnd== None):
            fCellOutBlankEnd = []
        else:
            fCellOutBlankEnd = self.fCellOutBlankEnd

        if (fCellOutSpecEndNoise == None):
            fCellOutSpecEndNoise = []
        else:
            fCellOutSpecEndNoise = self.fCellOutSpecEndNoise

        if (fCellOutBlankEndNoise == None):
            fCellOutBlankEndNoise = []
        else:
            fCellOutBlankEndNoise = self.fCellOutBlankEndNoise

        if (fCellOutSpecEndRM == None):
            fCellOutSpecEndRM = []
        else:
            fCellOutSpecEndRM = self.fCellOutSpecEndRM

        if (fCellOutBlankEndRM == None):
            fCellOutBlankEndRM = []
        else:
            fCellOutBlankEndRM = self.fCellOutBlankEndRM

        if (fFlowIn== None):
            fFlowIn = []
        else:
            fFlowIn = self.fFlowIn

        if (fFlowOut== None):
            fFlowOut = []
        else:
            fFlowOut = self.fFlowOut
