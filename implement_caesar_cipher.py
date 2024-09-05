def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted_message = caesar_cipher_encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
