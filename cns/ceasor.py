def caesar_cipher(content, shift):
    result = ""
    for char in content:
        if char.isalpha():

            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result

filepath = 'file1.txt'
with open (filepath,'r') as file:
    content = file.read()
shift = 3
encrypted_text = caesar_cipher(content, shift)
print("Encrypted:", encrypted_text)

# Decryption example:
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted:", decrypted_text)