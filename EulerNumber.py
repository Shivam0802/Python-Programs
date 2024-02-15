# Compute euler’s number. Use the Formula: e = 1 + 1/1! + 1/2! + …… 1/n!

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


LastTerm = int(input("Enter the last term of the series : "))
Temp = 0
for i in range(0, LastTerm + 1):
    result = factorial(i)
    Temp = float(Temp + float(1 / result))
print("After computing Euler's number : ", Temp)
