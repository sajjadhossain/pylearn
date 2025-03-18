def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def value_frequency(collection, value):
    return sum(1 for item in collection if item == value)
