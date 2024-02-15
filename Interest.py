Principle_Amount = float(input("Enter the principle amount : "))
Time = float(input("Enter the time (in years) : "))
Interest = float(input("Enter the interest : "))
N = int(input("Enter how much time taken [Compounded annually] : "))
SI = Principle_Amount * Time * Interest / 100
print("Simple Interest : ", SI)
CI = Principle_Amount * pow((1 + (Interest / N)), (N * Time))
print("Compound Interest : ", CI)
