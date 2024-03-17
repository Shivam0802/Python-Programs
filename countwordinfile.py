def count(file, word):
    try:
        with open(file, 'r') as file:
            content = file.read()
            occurrences = content.lower().count(word.lower())
            return occurrences
    except FileNotFoundError:
        print("File '{}' not found.".format(file))
        return -1


file_name = input("Enter the name of the text file: ")
word_count = input("Enter the word to count occurrences: ")

word_occurrences = count(file_name, word_count)

if word_occurrences != -1:
    print("Occurrences of ", word_count, " in ", file_name," file: ",word_occurrences)


