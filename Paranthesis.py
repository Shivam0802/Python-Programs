def linear_search(arr1, keys):
    for i in range(len(arr1)):
        if arr1[i] == keys:
            return i
    return -1


arr = list(map(int, input("Enter value with space ").split()))
key = int(input("Enter the key to search: "))
print("Found at index - ", linear_search(arr, key))


