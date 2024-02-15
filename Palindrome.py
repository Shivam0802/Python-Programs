Number = int(input("Enter the number : "))
temp = Number
rev = 0
while Number > 0:
    dig = int(Number % 10)
    rev = int((rev * 10) + dig)
    Number = int(Number / 10)
print("After computing Number is : ", rev)
if temp == rev:
    print("Number is Palindrome.....")
else:
    print("Number is not Palindrome.....")
