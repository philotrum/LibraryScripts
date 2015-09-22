# -*- coding: utf-8 -*
"""
Created 20150501

@author: G. Kettlewell

Functions to make generating graphs on a matplotlib plot easier and more consistent.
"""

from scipy.stats import norm
import matplotlib.mlab as mlab

def DrawHist(inFig, inPos, inData, inNumBins = 100, inXLabel = '',
              inXMin = 'NA', inXMax = 'NA', inYMin = 'NA', inYMax = 'NA', inShareX_Ax = 'NA'):
    """ Add a histogram to a figure.

        Arguments:
            inFig:      The figure to which the plot is added
            inPos:      The position to place the plot on the figure
            inData:     The data to plot
            inNumBins:  The number of bins for the histogram
            inXLabel:   The label for the plot
            inXMin:     The x axis minimum
            inXMax:     The x axis maximum
            inXMin:     The y axis minimum
            inXMin:     The y axis maximum

        If inXMin == NA then the x axis won't be scaled.
        If iYXMin == NA then the y axis won't be scaled.

        Returns the axis that has just been added.
    """

    # Check to see if inShareX_Ax is a string. If it is
    # then we haven't passed in an axis to sharem so just
    # plot it.
    if (isinstance(inShareX_Ax, str)):
        ax = inFig.add_subplot(inPos)
    # Otherwise set up the shared axis
    else:
        ax = inFig.add_subplot(inPos, sharex=inShareX_Ax)
    n, bins, patches = ax.hist(inData, inNumBins, normed=True, alpha=0.75)
    if (inXMin != 'NA'):
        ax.set_xlim(inXMin, inXMax)
    if (inYMin != 'NA'):
        ax.set_ylim(inYMin, inYMax)

    # best fit of data
    (mu, sigma) = norm.fit(inData)

    # add a 'best fit' line
    y = mlab.normpdf(bins, mu, sigma)
    ax.plot(bins, y, 'r--', linewidth=2)

    ax.set_xlabel(inXLabel + ' ' + r'$\mathrm{IQ:}\ \mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))

    ax.grid(True)

    return ax

def DrawScatter(inFig, inPos, inDates, inData, inYLabel = '',
                 inXMin = 'NA', inXMax = 'NA', inYMin = 'NA', inYMax = 'NA', inShareX_Ax = 'NA'):

    """ Add a scatter graph to a figure.

        Arguments:
            inFig:      The figure to which the plot is added
            inPos:      The position to place the plot on the figure
            inData:     The data to plot
            inNumBins:  The number of bins for the histogram
            inXLabel:   The label for the plot
            inXMin:     The x axis minimum
            inXMax:     The x axis maximum
            inXMin:     The y axis minimum
            inXMin:     The y axis maximum

        If inXMin == NA then the x axis won't be scaled.
        If iYXMin == NA then the y axis won't be scaled.

        Returns the axis that has just been added.
    """

    # Check to see if inShareX_Ax is a string. If it is
    # then we haven't passed in an axis to sharem so just
    # plot it.
    if (isinstance(inShareX_Ax, str)):
        ax = inFig.add_subplot(inPos)
    # Otherwise set up the shared axis
    else:
        ax = inFig.add_subplot(inPos, sharex=inShareX_Ax)
    ax.scatter(inDates[:len(inData)], inData, marker='+')
    ax.set_ylabel(inYLabel)
    if (inXMin != 'NA'):
        ax.set_xlim(inXMin, inXMax)
    if (inYMin != 'NA'):
        ax.set_ylim(inYMin, inYMax)

    ax.grid(True)

    return ax
