letters='abcdefghijklmnopqrsstuvwxyz'
num_letter=len(letters)

def encrypt(plaintext,key):
    ciphertext=''
    for letter in plaintext:
        letter=letter.lower()
        if not letter==' ':
            index=letters.find(letter)
            if index==-1:
                ciphertext += letter
            else:
                new_index= index+key
                if new_index >= num_letter:
                    new_index -= num_letter
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext,key):
    plaintext=''
    for letter in ciphertext:
        letter=letter.lower()
        if not letter==' ':
            index=letters.find(letter)
            if index==-1:
                ciphertext += letter
            else:
                new_index= index-key
                if new_index < 0:
                    new_index +=num_letter
                ciphertext += letters[new_index]
    return ciphertext



print()
print("*** CAESER CIPHER ***")
print()

print("Do u want to encrypt or decrypt?")
user_input=input('e/d: ').lower()
print()

if user_input=='e':
    print("ENCRYPTION MODE SELECTED")
    print()
    key=int(input("enter the key (1 through 26):"))
    text=input("Enter the text to encrypt:")
    ciphertext=encrypt(text,key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input=='d':
    print("DECRYPTION MODE SELECTED")
    print()
    key=int(input("enter the key (1 through 26):"))
    text=input("Enter the text to decrypt:")
    plaintext=decrypt(text,key)
    print(f'PLAINTEXT: {plaintext}')