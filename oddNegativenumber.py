def filter_list(nums):
    list_filtered = []
    # Loop through the list to filter out negative numbers
    for num in nums:
        if num >= 0 and num % 2 == 0:
            list_filtered.append(num)
    return list_filtered


Num = []
size = int(input("Enter the size of the list : "))
print("Enter the element in List : ")
for i in range(0, size):
    ele = int(input())
    Num.append(ele)
print("Element present : ", Num)
filtered_list = filter_list(Num)
print("Filtered list after removing odd and negative numbers:", filtered_list)



