word_to_count = {}
sentence = input("Text: ")
words = sentence.split(" ")
print(words)
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
print(word_to_count)