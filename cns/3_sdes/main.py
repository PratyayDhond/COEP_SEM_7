# Helper functions for S-DES implementation
def permute(bits, permutation):
    """Permute the bits according to the permutation table."""
    return [bits[p - 1] for p in permutation]

def left_shift(bits, n):
    """Circular left shift of the bits."""
    return bits[n:] + bits[:n]

def xor(bits1, bits2):
    """Perform XOR operation between two bit lists."""
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

# Key generation function
def key_generation(key_10):
    """Generate two 8-bit keys from the 10-bit key."""
    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]  # P10 permutation
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]         # P8 permutation
    
    # Apply P10 permutation and split into two halves
    permuted_key = permute(key_10, p10)
    left, right = permuted_key[:5], permuted_key[5:]

    # Perform LS-1 (left shift by 1 bit)
    left, right = left_shift(left, 1), left_shift(right, 1)

    # Generate first 8-bit key (K1)
    k1 = permute(left + right, p8)

    # Perform LS-2 (left shift by 2 bits)
    left, right = left_shift(left, 2), left_shift(right, 2)

    # Generate second 8-bit key (K2)
    k2 = permute(left + right, p8)

    return k1, k2

# Sample test case
key_10 = [1, 0, 1, 0, 0, 0, 1, 1, 1, 0]  # 10-bit key example
k1, k2 = key_generation(key_10)

print("Generated Keys:")
print("K1:", k1)
print("K2:", k2)
