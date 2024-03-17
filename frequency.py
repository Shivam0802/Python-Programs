def count_word_frequency(sentence):
    words = sentence.split()
    word_freq = {}
    for i in words:
        if i in word_freq:
            word_freq[i] += 1
        else:
            word_freq[i] = 1
    return word_freq


input_sentence = input("Enter a sentence: ")
word_frequency = count_word_frequency(input_sentence)
print("Word frequency in the sentence:")
for word, frequency in word_frequency.items():
    print(word, " : ", frequency)


