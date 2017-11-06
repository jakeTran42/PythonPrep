import random
import sys

def dictionaryFile(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
    return words

def randomDictionary(clean_text, sentence_len):
    randomSentence = []
    for index in range(0, sentence_len):
        random_index = random.randint(0, len(clean_text) - 1)
        randomSentence.append(clean_text[random_index])
    sentence = " ".join(randomSentence)
    return sentence





if __name__ == '__main__':
    inputs = sys.argv[1]

    cleanText = dictionaryFile('/usr/share/dict/words')
    print(randomDictionary(cleanText, int(inputs)))
