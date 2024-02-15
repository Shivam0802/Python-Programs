# Print all Numbers in a range Divisible by a Given Number

StartPoint = int(input("Enter the start point of Range : "))
LastPoint = int(input("Enter the last point of Range : "))
Number = int(input("Enter the number by which you want to divide : "))
for i in range(StartPoint, LastPoint + 1):
    if i % Number == 0:
        print("Number divisible by ", Number, " : ", i)
