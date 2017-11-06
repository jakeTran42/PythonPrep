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

if __name__ == '__main__':
    cleanFiles = cleanText('text.txt')
    his_Dict = histogramDictionary(cleanFiles)
    his_Array = histogramNestedArray(cleanFiles)
    histogramTuples = histogramTuples(cleanFiles)
    print(his_Array)
