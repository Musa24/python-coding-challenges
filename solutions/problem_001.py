def count_words(words):
    output = {}
    for word in words:
        word = word.lower()
        if word in output.keys():
            output[word] = output[word]+1
        else:
            output[word] = 1
    return output

# example
words = "Apple orange apple banana"
words = words.split()
print(count_words(words))  # {'orange': 1, 'apple': 2, 'banana': 1}