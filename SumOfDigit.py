# Program to find sum of digits in a number.

Num = input("Write a number : ")
Sum = 0
for i in Num:
    Sum = Sum + int(i)
print("Sum of Digits in a number : ", Sum)
