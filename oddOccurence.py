def find_odd_occurrence(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for key, value in count.items():
        if value % 2 != 0:
            print(key, "occurring", value, "odd no. of times.")


my_list = []
size = int(input("Enter the size of the list : "))
print("Enter the element in List : ")
for i in range(0, size):
    ele = int(input())
    my_list.append(ele)
print("Element present : ", my_list)
find_odd_occurrence(my_list)


