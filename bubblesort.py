def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


my_list = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
print("Original list:", my_list)
bubble_sort(my_list)
print("List sorted in ascending order using bubble sort:", my_list)


