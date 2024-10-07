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

    # Convert the encrypted binary to a string of readable characters
    readable_output = binary_to_string(encrypted_binary)

    print(f"Encrypted output: {readable_output}")
