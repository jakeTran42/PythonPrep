import sys

def cleanText(filename):
    with open(filename, 'r') as f:
        clean_text = f.read().strip().replace(',', '').replace('.', '').replace('?', '')
    return clean_text

def histogramDictionary(cleanText):
    text = cleanText.lower().split()
    histogram = {}
    for word in text:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def histogramNestedArray(cleanText):
    text = cleanText.lower().split()
    histogram = []
    for newWord in text:
        newEntry = text[text.index(newWord)]
        count = text.count(newWord)
        histogram.append([newEntry, count])

    for word in histogram:
        count = histogram.count(word)
        if count != 1:
            histogram.remove(word)
    return histogram


def histogramTuples(cleanText):
    text = cleanText.lower().split()
    histogram = []
    for newWord in text:
        newEntry = text[text.index(newWord)]
        count = text.count(newWord)
        histogram.append((newEntry, count))

    for word in histogram:
        count = histogram.count(word)
        if count != 1:
            histogram.remove(word)
    return histogram

def frequency(histogram, word):
    if word in histogram:
        return histogram[word]
    else:
        return 0

def unique_words(histogram):
    types =[]
    for word in histogram:
        if histogram[word] == 1:
            types.append(word)
        else:
            pass
    return types, (len(histogram) - 1)


if __name__ == '__main__':
    cleanFiles = cleanText('text.txt')
    his_Dict = histogramDictionary(cleanFiles)
    his_Array = histogramNestedArray(cleanFiles)
    histogramTuples = histogramTuples(cleanFiles)
    freq_tokens = frequency(his_Dict, "the")
    print("The Word appear '" + str(freq_tokens) + "' times.")
    unique_types = unique_words(his_Dict)
    print("The unique words are " + str(unique_types[0]) + "\n and there are '" + str(unique_types[1]) + "' unique words")
