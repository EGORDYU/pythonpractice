alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




cont = "yes"

def encrypt(text,shift):

    encrypted_text = ""
    
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            shifted = (position + shift) % 26
            encrypted_text += alphabet[shifted]
        else:
            encrypted_text += letter
    
    print(encrypted_text)
    


def decrypt(text,shift):

    decrypted_text = ""
    encrypted_text = text

    for letter in encrypted_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            shifted = (position - shift) % 26
            decrypted_text += alphabet[shifted]
        else:
            decrypted_text += letter
    
    print(decrypted_text)
    



while cont == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    if direction == "encode":
        encrypt(text,shift)
        cont = input("want to continue? yes or no")

    elif direction == "decode":
        decrypt(text,shift)
        cont = input("want to continue? yes or no")
        