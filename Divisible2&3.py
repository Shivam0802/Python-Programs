# Print all integers that are not divisible by either 2 or 3 and lie between 1 and 50.

StartIndex = 1
LastIndex = 51
for i in range(StartIndex, LastIndex):
    if i % 2 != 0 and i % 3 != 0:
        print("Number that is not divisible by 2 and 3 : ", i)
