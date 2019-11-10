print("Please enter a message you would like to encrypt")
plainText = input("Message: ")
k = int(input("Shift amount: "))
cipherText=""

while k < 32:
    k += 96
while k > 127:
    k -= 96
