def display_student_info(student, admission):
    if admission in student:
        print("Admission Number:", admission)
        print("Roll Number:", student[admission]['Roll_Number'])
        print("Name:", student[admission]['Name'])
        print("Marks:", student[admission]['Marks'])
    else:
        print("Student with admission number ", admission, " not found.")


student_info = {}
size = int(input("Enter the no of student present : "))
for i in range(0, size):
    add_no = input("Enter the admission number : ")
    student_info[add_no] = {}
    Name = input("Enter name : ")
    Roll_Number = int(input("Enter Roll number : "))
    Marks = int(input("Enter marks : "))
    student_info[add_no]["Name"] = Name
    student_info[add_no]["Roll_Number"] = Roll_Number
    student_info[add_no]["Marks"] = Marks
print(student_info)
admission_number = input("Enter admission number to display information: ")
display_student_info(student_info, admission_number)


