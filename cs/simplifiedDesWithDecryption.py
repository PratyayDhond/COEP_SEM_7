import base64

class SimplifiedDES:
    # Simplified DES parameters
    NUM_ROUNDS = 2
    PERMUTATION = [2, 6, 3, 1, 4, 8, 5, 7]
    INVERSE_PERMUTATION = [4, 1, 3, 5, 7, 2, 8, 6]
    SBOX = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [2, 1, 3, 0]
    ]

    @staticmethod
    def permute(input_bits, permutation):
        return ''.join(input_bits[i - 1] for i in permutation)

    @staticmethod
    def sbox_lookup(input_bits):
        row = int(input_bits[0] + input_bits[3], 2)
        col = int(input_bits[1] + input_bits[2], 2)
        return format(SimplifiedDES.SBOX[row][col], '02b')

    @staticmethod
    def generate_subkeys(key):
        return [key[:4], key[4:]]

    @staticmethod
    def f_function(right, subkey):
        combined = bin(int(right, 2) ^ int(subkey, 2))[2:].zfill(4)
        return SimplifiedDES.sbox_lookup(combined)

    @classmethod
    def encrypt(cls, plaintext, key):
        # Initial permutation
        permuted_input = cls.permute(plaintext, cls.PERMUTATION)
        left, right = permuted_input[:4], permuted_input[4:]

        # Generate subkeys
        subkeys = cls.generate_subkeys(key)

        # Two rounds of processing
        for round in range(cls.NUM_ROUNDS):
            f_result = cls.f_function(right, subkeys[round])
            left = bin(int(left, 2) ^ int(f_result, 2))[2:].zfill(4)  # XOR left with f_result
            if round < cls.NUM_ROUNDS - 1:
                left, right = right, left  # Swap left and right

        # Combine the two halves
        combined = right + left

        # Final permutation
        return cls.permute(combined, cls.INVERSE_PERMUTATION)

    @classmethod
    def decrypt(cls, ciphertext, key):
        # Initial permutation
        permuted_input = cls.permute(ciphertext, cls.PERMUTATION)
        left, right = permuted_input[:4], permuted_input[4:]

        # Generate subkeys (in reverse order for decryption)
        subkeys = cls.generate_subkeys(key)[::-1]

        # Two rounds of processing
        for round in range(cls.NUM_ROUNDS):
            f_result = cls.f_function(right, subkeys[round])
            left = bin(int(left, 2) ^ int(f_result, 2))[2:].zfill(4)  # XOR left with f_result
            if round < cls.NUM_ROUNDS - 1:
                left, right = right, left  # Swap left and right

        # Combine the two halves
        combined = right + left

        # Final permutation
        return cls.permute(combined, cls.INVERSE_PERMUTATION)


def string_to_binary(string):
    return ''.join(format(ord(char), '08b') for char in string)

def binary_to_string(binary):
    # Split binary into chunks of 8 bits (1 byte)
    return ''.join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))

if __name__ == "__main__":
    # Input a human-readable string
    input_string = input("Enter a string to encrypt: ")

    # Key
    key = "10101010"  # Example key

    encrypted_binary = ''
    
    # Encrypt each character in the input string
    for char in input_string:
        binary_char = format(ord(char), '08b')  # Convert to binary
        ciphertext = SimplifiedDES.encrypt(binary_char, key)  # Encrypt
        encrypted_binary += ciphertext  # Concatenate encrypted binary

    # Convert the encrypted binary to a bytes object
    encrypted_bytes = int(encrypted_binary, 2).to_bytes((len(encrypted_binary) + 7) // 8, byteorder='big')
    
    # Encode the bytes to a Base64 string
    base64_encoded = base64.b64encode(encrypted_bytes).decode('utf-8')
    
    print(f"Encrypted output (Base64): {base64_encoded}")

    # Decode the Base64 string back to bytes
    decrypted_bytes = base64.b64decode(base64_encoded)
    
    # Convert the decrypted bytes back to binary string
    decrypted_binary = ''.join(format(byte, '08b') for byte in decrypted_bytes)

    # Decrypt the decrypted binary back to the original string
    decrypted_string = ''
    for i in range(0, len(decrypted_binary), 8):
        encrypted_char = decrypted_binary[i:i + 8]
        decrypted_char = SimplifiedDES.decrypt(encrypted_char, key)
        decrypted_string += chr(int(decrypted_char, 2))

    print(f"Decrypted output: {decrypted_string}")
