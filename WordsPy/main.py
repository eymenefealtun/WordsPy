import random


def get_random_words(source, numberOfWords):
    resultArray = []

    for i in range(numberOfWords):
        resultArray.append(source[random.randint(0, len(source) - 1)])

    return resultArray


def get_random_word(source):
    return source[random.randint(0, len(source) - 1)]

