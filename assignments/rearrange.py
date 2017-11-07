import random
import sys

def rearrange(inputs):
    words = []
    while len(inputs) > 0:
        random_index = random.randint(0, len(inputs) - 1)
        words.append(inputs[random_index])
        del inputs[random_index]

    return " ".join(words)

def stringReversal(inputs):
    inverseString = []
    maxIndex = len(inputs)
    for index in range(0, len(inputs)):
        inverseString.append(inputs[maxIndex - 1])
        maxIndex -= 1
    return inverseString
    # return inputs[::-1] Easy Solution here


if __name__ == '__main__':
    inputs = sys.argv[1:]
    # print(rearrange(inputs))
    print(stringReversal(inputs))
