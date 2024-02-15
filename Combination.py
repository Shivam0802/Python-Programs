def Combination(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if i != j and j != k and i != k:
                    print(arr[i], arr[j], arr[k])


a = int(input("Enter the First digit : "))
b = int(input("Enter the second digit : "))
c = int(input("Enter the Third digit : "))
Combination([a, b, c])


