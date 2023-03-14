message = input("what is your message: ")
encryptedMessage = "";
decryptedMessage = "";

for c in message:
    encryptedMessage = encryptedMessage + chr(ord(c) + key)
 
print (encryptedMessage)


for c in encryptedMessage:
    decryptedMessage = decryptedMessage + chr(ord(c) - key)
 
print (decryptedMessage)
