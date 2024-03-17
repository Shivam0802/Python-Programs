def find_second_largest(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[1]


Num = []
size = int(input("Enter the size of the list : "))
print("Enter the element in List : ")
for i in range(0, size):
    ele = int(input())
    Num.append(ele)
print("Element present : ", Num)
second_largest = find_second_largest(Num)
print(f"The second largest element in the list is: ",second_largest)


