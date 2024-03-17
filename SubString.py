def is_substring_present(main, sub):
    if sub in main:
        return True
    else:
        return False


main_string = input("Enter the main string: ")
substring = input("Enter the substring to search for: ")

if is_substring_present(main_string, substring):
    print("The substring ", substring, " is present in the main string.")
else:
    print("The substring ", substring, "is not present in the main string.")


