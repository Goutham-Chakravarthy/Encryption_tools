def vigenere_encrypt(plaintext, keyword):
    ciphertext = "" 
    keyword = keyword.upper()  

    for i in range(len(plaintext)):  
        char = plaintext[i]  
        if char.isalpha():  
            shift = ord(keyword[i % len(keyword)]) - ord('A') 
            encrypted_char = chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))  
        else:
            ciphertext += char  
    return ciphertext 


def vigenere_decrypt(ciphertext, keyword):
    plaintext = "" 
    keyword = keyword.upper()  

    for i in range(len(ciphertext)): 
        char = ciphertext[i]  
        if char.isalpha(): 
            shift = ord(keyword[i % len(keyword)]) - ord('A')  
            decrypted_char = chr((ord(char.upper()) - ord('A') - shift + 26) % 26 + ord('A'))  
            plaintext += decrypted_char  
        else:
            plaintext += char  
    return plaintext  


# Main program
print("Choose an option:") 
print("1. Encrypt")
print("2. Decrypt")
print("3. Exit")

while True:
    choice = input("Enter your choice : ")  # Take the user's choice as input.


    if choice == "1":  # If the user chooses encryption.
        plaintext = input("Enter the plaintext: ")  # Ask for the plaintext.
        keyword = input("Enter the keyword: ")  # Ask for the keyword.
        ciphertext = vigenere_encrypt(plaintext, keyword)  # Encrypt the plaintext using the provided keyword.
        print("\nEncrypted text (Ciphertext):", ciphertext)  # Display the encrypted text.


    elif choice == "2":  # If the user chooses decryption.
        ciphertext = input("Enter the ciphertext: ")  # Ask for the ciphertext.
        keyword = input("Enter the keyword: ")  # Ask for the keyword.
        plaintext = vigenere_decrypt(ciphertext, keyword)  # Decrypt the ciphertext using the provided keyword.
        print("\nDecrypted text (Plaintext):", plaintext)  # Display the decrypted text.

    elif choice == "3":  # If the user chooses decryption.
       print("EXIT")
       break

    else:  # If the user enters an invalid choice.
        print("Invalid choice! Please choose 1 or 2.")  # Display an error message.1


