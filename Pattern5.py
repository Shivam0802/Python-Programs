n = int(input("Enter the size of pattern : "))
for i in range(1, n + 1):
    for j in range(1, (n + 1) - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(n, end=" ")
        n = n - 1
    print()
