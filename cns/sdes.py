# Helper functions for S-DES implementation
def permute(bits, permutation):
    permuted_bits = []
    for p in permutation:
        permuted_bits.append(bits[p - 1])
    return permuted_bits


def left_shift(bits, n):
    return bits[n:] + bits[:n]


def xor(bits1, bits2):
    result = []
    for b1, b2 in zip(bits1, bits2):
        result.append(b1 ^ b2)
    return result


def sbox(input_bits, sbox_table):
    row = (input_bits[0] << 1) + input_bits[3]
    col = (input_bits[1] << 1) + input_bits[2]
    return [int(b) for b in format(sbox_table[row][col], '02b')]


def fk(bits, subkey):
    # Split the bits into left and right halves
    left, right = bits[:4], bits[4:]
    
    # Expansion permutation (E/P)
    ep = [4, 1, 2, 3, 2, 3, 4, 1]
    expanded_right = permute(right, ep)
    
    # XOR with subkey
    xor_result = xor(expanded_right, subkey)
    
    # S-Box substitution
    s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    s1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
    
    left_sbox = sbox(xor_result[:4], s0)
    right_sbox = sbox(xor_result[4:], s1)
    
    # Combine results of S-Boxes and apply P4 permutation
    p4 = [2, 4, 3, 1]
    p4_result = permute(left_sbox + right_sbox, p4)
    
    # XOR with left half
    result = xor(left, p4_result)
    
    # Return the result concatenated with the unchanged right half
    return result + right


def sdes_encrypt(plaintext, k1, k2):
    ip = [2, 6, 3, 1, 4, 8, 5, 7]  # Initial permutation
    ip_inv = [4, 1, 3, 5, 7, 2, 8, 6]  # Inverse initial permutation
    
    # Apply initial permutation
    permuted_bits = permute(plaintext, ip)
    
    # Round 1 with K1
    round1 = fk(permuted_bits, k1)
    
    # Swap halves
    swapped = round1[4:] + round1[:4]
    
    # Round 2 with K2
    round2 = fk(swapped, k2)
    
    # Apply inverse permutation
    ciphertext = permute(round2, ip_inv)
    return ciphertext


def sdes_decrypt(ciphertext, k1, k2):
    # The decryption process is the reverse of encryption
    ip = [2, 6, 3, 1, 4, 8, 5, 7]
    ip_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    
    # Apply initial permutation
    permuted_bits = permute(ciphertext, ip)
    
    # Round 1 with K2 (keys are reversed in decryption)
    round1 = fk(permuted_bits, k2)
    
    # Swap halves
    swapped = round1[4:] + round1[:4]
    
    # Round 2 with K1
    round2 = fk(swapped, k1)
    
    # Apply inverse permutation
    plaintext = permute(round2, ip_inv)
    return plaintext


def key_generation(key_10):
    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]  
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]         
    
    permuted_key = permute(key_10, p10)
    left, right = permuted_key[:5], permuted_key[5:]
    left, right = left_shift(left, 1), left_shift(right, 1)
    k1 = permute(left + right, p8)
    left, right = left_shift(left, 2), left_shift(right, 2)
    k2 = permute(left + right, p8)
    return k1, k2


# Example usage
key_10 = [1, 0, 1, 0, 0, 0, 1, 1, 1, 0]
k1, k2 = key_generation(key_10)

# Input plaintext (8 bits)
plaintext = [1, 0, 0, 1, 0, 1, 1, 1]  # Example plaintext

# # Encryption
# ciphertext = sdes_encrypt(plaintext, k1, k2)
# print("Ciphertext:", ciphertext)

# # Decryption
# decrypted_text = sdes_decrypt(ciphertext, k1, k2)
# print("Decrypted Text:", decrypted_text)

def text_to_bits(text):
    """Convert a string into a list of bits."""
    bits = []
    for char in text:
        binary_char = format(ord(char), '08b')  # Convert to 8-bit binary
        bits.extend([int(bit) for bit in binary_char])
    return bits


def bits_to_text(bits):
    """Convert a list of bits back into a string."""
    text = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        char = chr(int("".join(map(str, byte)), 2))  # Convert 8 bits to character
        text += char
    return text


def process_text(input_text, k1, k2):
    """Encrypt and decrypt the user input text and display results."""
    print(f"Input Text: {input_text}")
    
    # Convert the text to bits
    plaintext_bits = text_to_bits(input_text)
    print(f"Plaintext Bits: {plaintext_bits}")
    
    # Perform encryption
    ciphertext_bits = []
    for i in range(0, len(plaintext_bits), 8):  # Process 8 bits at a time
        block = plaintext_bits[i:i+8]
        ciphertext_bits.extend(sdes_encrypt(block, k1, k2))
        ciphertext_text = bits_to_text(ciphertext_bits)
    print(f"Ciphertext Bits: {ciphertext_bits}")

    
    # Perform decryption
    decrypted_bits = []
    for i in range(0, len(ciphertext_bits), 8):  # Process 8 bits at a time
        block = ciphertext_bits[i:i+8]
        decrypted_bits.extend(sdes_decrypt(block, k1, k2))
    decrypted_text = bits_to_text(decrypted_bits)
    
    print(f"Decrypted Bits: {decrypted_bits}")
    print(f"Ciphertext Text: {ciphertext_text}")
    print(f"Decrypted Text: {decrypted_text}")


# Example usage
key_10 = [1, 0, 1, 0, 0, 0, 1, 1, 1, 0]
k1, k2 = key_generation(key_10)

# Input plaintext
input_text = input("Enter plaintext to encrypt: ")

# Process the text
process_text(input_text, k1, k2)
