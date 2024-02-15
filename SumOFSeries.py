# Compute the Value of 1 + 2 + 3 + ....... + n

LastTerm = int(input("Enter the Last Term of the series : "))
Sum = 0
for i in range(1, LastTerm + 1):
    Sum = Sum + i
print("The sum of ", LastTerm, " terms in series : ", Sum)
