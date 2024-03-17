def remove_key(dictionary, key_element):
    if key_element in dictionary:
        del dictionary[key_element]
        print("Key ", key_element, " removed successfully.")
    else:
        print("Key ", key_element, " not found in the dictionary.")


my_dict = {}
size = int(input("Enter the size of dictionary : "))
for i in range(0, size):
    print("Enter key ", i + 1, " : ", end=" ")
    key = input()
    print("Enter value ", i + 1, " : ", end=" ")
    value = input()
    my_dict[key] = value
print("Original dictionary:", my_dict)
key_to_remove = input("Enter the key to remove from the dictionary: ")
remove_key(my_dict, key_to_remove)
print("Dictionary after removal:", my_dict)


