from builtins import int

FirstTerm = 0
SecondTerm = 1
num = int(input("Enter the number of terms : "))
i = 0
print("Fibonacci Series for ", num, " : ")
while i < num:
    NextTerm = int(FirstTerm + SecondTerm)
    print(NextTerm, end=" ")
    FirstTerm = SecondTerm
    SecondTerm = NextTerm
    i = i + 1
print("\nThis is the Fibonacci series of ", num, " terms.....")
