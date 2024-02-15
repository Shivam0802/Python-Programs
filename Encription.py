# Write a program that encrypts a message by adding a key value to every character.
# ord(): This function convert character into ASCII code.
# chr(): This function convert ASCII code into character.

Message = input("Enter the message : ")
EncryptMessage = 0
print("Message after encryption : ",end=" ")
for i in Message:
    EncryptMessage = chr(ord(i) + 3)
    print(EncryptMessage, end="")
