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


def getNextWord(dictionary):

    ''' Choose the next word to append for sentence '''

    nextWordHistogram = wordProbability(dictionary)

    getTotalWord = totalWords(dictionary)

    random_num = random.randint(1, getTotalWord)
    for key, value in nextWordHistogram.items():
        if value < random_num:
            random_num -= value
        else:
            return key

def markovDictogram(text):
    wordList = text.split()
    markovDict = {}
    for wordIndex in range(len(wordList) - 2):
        currentTuple = tuple((wordList[index]) for index in range(wordIndex, wordIndex + 2))
        nextWord = wordList[wordIndex + 2]

        if currentTuple in markovDict:
            markovDict[currentTuple].add_count(nextWord)
        else:
            markovDict[currentTuple] = Dictogram([nextWord])

    return markovDict

def createMarkovChain(dictionary):
    ''' Return sentences '''

    dictionaryKeys = [key for key, value in dictionary.items()]
    sentenceArray = list(dictionaryKeys[random.randint(0, len(dictionaryKeys) - 1)])

    for wordIndex in range(10):
        key  = tuple((sentenceArray[index]) for index in range(wordIndex, wordIndex + 2))

        if key in dictionary:
            wordDict = dictionary[key]
            next_Word = getNextWord(wordDict)
            sentenceArray.append(next_Word)

        return ' '.join(sentenceArray)


if __name__ == "__main__":
    text = 'Miss Watson she kept pecking at me, and it got tiresome and lonesome. By and by they fetched the niggers in and had prayers. I hadn’t no confidence.  You do that when you’ve lost a horseshoe that'

    markov = markovDictogram(text)
    print(createMarkovChain(markov))
