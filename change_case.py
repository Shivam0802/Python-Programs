def change_case(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].upper()
        else:
            result += s[i]
    return result


input_string = input("Enter a string: ")
capitalized_string = change_case(input_string)
print("String with every other letter capitalized:", capitalized_string)

