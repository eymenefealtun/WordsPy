import random


def get_random_words(source, number_of_words):
    result = []

    for i in range(number_of_words):
        result.append(source[random.randint(0, len(source) - 1)])

    return result


def get_random_word(source):
    return source[random.randint(0, len(source) - 1)]
