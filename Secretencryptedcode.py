Hello = """Hello Agent Jhamb
If you're reading this then I must have sent you an email that is encrypted or 
you want to encrypt a message. You can use this program to decrypt it"""
print(Hello)

key = 4
message = input("What is your message: ")
key = int(input('Enter the cryptic key:'))

# Initialize encryptedMessage as a global variable
encryptedMessage = ""

def encrypt():
    global encryptedMessage
    encryptedMessage = ""
    for c in message:
        encryptedMessage += chr(ord(c) + key)
    print(f"Encrypted Message: {encryptedMessage}")
    return encryptedMessage

def decrypt():
    global message
    decryptedMessage = ""
    for c in message:
        decryptedMessage += chr(ord(c) - key)
    print(f"Decrypted Message: {decryptedMessage}")
    return decryptedMessage

choice = input("Do you want to encrypt (1) message or decrypt (2) message: ")

if choice == "1":
    encryptedMessage = encrypt()
elif choice == "2":
        decrypt()
else:
    print("That is the wrong answer. Please type the correct number.")
