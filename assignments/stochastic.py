from histogram import histogramNestedArray
from histogram import histogramDictionary
from histogram import cleanText
import random

# def weighted_array(his_Array):
#     weightedHist = []
#     total = sum(word[1] for word in his_Array)
#     for word in his_Array:
#         weightedHist.append([word[0], word[1]/total])
#     return weightedHist
#
#
# def stochastic_sampling(weighted_hist):
#     cum_weight = 0
#     for word in weighted_hist:
#         cum_weight += word[1]
#     return cum_weight

def totalWord(dictionary):
    total_words = 0
    for word in dictionary:
        total_words += dictionary[word]
    return total_words

def getRandomWord(dictionary, totalWords):
    random_num = random.randint(1, totalWords)
    for word in dictionary:
        if dictionary[word] < random_num:
            random_num -= dictionary[word]
        else:
            return word


if __name__ == '__main__':
    textFiles = cleanText('text.txt')
    hist_dictionary = histogramDictionary(textFiles)
    total_words = totalWord(hist_dictionary)

    # weightOfArray = weighted_array(histogramNestedArray(textFiles))
    # print(weighted_array(histogramNestedArray(cleanText('text.txt'))))
    # print(stochastic_sampling(weightOfArray))

    print(getRandomWord(hist_dictionary, total_words))
