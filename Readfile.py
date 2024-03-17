def count_lines_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print("File ", file_name, " not found.")
        return -1


file1_name = input("Enter the name of the first file: ")
file2_name = input("Enter the name of the second file: ")

file1_lines = count_lines_in_file(file1_name)
file2_lines = count_lines_in_file(file2_name)

if file1_lines != -1:
    print("Total number of lines in file1_lines : ", file1_lines)
if file2_lines != -1:
    print("Total number of lines in file2_lines : ", file2_lines)


