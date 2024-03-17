def isPalindrome(string):
    char = string.split(" ")
    string_list = list(char)
    for i in string_list:
        for j in i:
            return j == j[::-1]


s = input("Enter the string : ")
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")


