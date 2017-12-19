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

# def getRandomWord(histogram, totalWord):
#
#     ''' Get random word out of histogram '''
#
#     random_num = random.randint(1, totalWords)
#     for key, value in histogram.items():
#         if value < random_num:
#             random_num -= value
#         else:
#             return key

# def startingWord(dictionary):
#
#     ''' Pick a word to start sentence '''
#
#     words = []
#     for key in dictionary:
#         words.append(key)
#     randIndex = random.randint(0, len(words))
#     return word_list[random_index]
