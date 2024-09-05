def caesar_cipher(text: str, shift: int, encode:bool=True) -> str:
    result = ""
    
    if not encode:
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += chr((ord(char) + shift ) % (256*256)) # 256*256 to support episilon and overall unicode and emoji characters    
    return result

plain_text = "Hello, World!"
shift = 6

encoded_text = caesar_cipher(plain_text, shift, encode=True)
print(f"Cipher Text: {encoded_text}")

decoded_text = caesar_cipher(encoded_text, shift, encode=False)
print(f"Plain Text: {decoded_text}")
