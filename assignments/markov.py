import random
from dictogram import Dictogram

def totalWords(histogram):

    ''' Total Word of Hist'''

    count = 0
    for key, value in histogram.items():
        count += value
        return count

def wordProbability(histogram):
    total = totalWords(histogram)
    count = 0
    totalValue = 0
    newHist = {}
    for key, value in histogram.items():
        weightedValue = (value / total)
        totalValue = weightedValue + count
        newHist[key] = value
        count += weightedValue
    return newHist
