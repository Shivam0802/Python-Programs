def compare(first, second):
    first_set = set(first)
    second_set = set(second)
    letters = first_set.difference(second_set)
    return letters


first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")
result = compare(first_string, second_string)
print("Letters in the first string but not in the second string:", result)


