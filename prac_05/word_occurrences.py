word_to_count = {}
sentence = input("Text: ")
words = sentence.split(" ")
words.sort()

"""Count occurrence of words"""
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

"""Finding the longest word"""
longest_length = 0
for word in words:
    length = len(word)
    if len(word) > longest_length:
        longest_length = len(word)
    else:
        longest_length = longest_length

"""Display the count of the words"""
for word, count in word_to_count.items():
    print("{:{}} : {}".format(word, longest_length, count))
