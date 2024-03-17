def append_to_file(file, content):
    with open(file, 'a') as file:
        file.write(content + '\n')
        print("String appended to ", file, " successfully.")


file_name = input("Enter the name of the file to append to: ")
input_string = input("Enter the string to append to the file: ")
append_to_file(file_name, input_string)


