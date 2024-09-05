import numpy as np
from sympy import Matrix

DEFAULT_MODULO = 26
START_VALUE = 65

def matrix_multiply(key_matrix: list[int], text_matrix: list[int]) -> str:
    n = len(key_matrix)
    result_vector = [0] * n

    for i in range(n):
        for j in range(n):
            result_vector[i] += key_matrix[i][j] * text_matrix[j]
    
    return result_vector

def caculate_inverse_matrix(key_matrix: list[int]) -> list[int]:
    det = int(np.round(np.linalg.det(key_matrix)))  # Determinant of the matrix
    det_inv = pow(det, -1, DEFAULT_MODULO)  # Modular inverse of the determinant
    np_matrix = det_inv * np.array(Matrix(key_matrix).adjugate()) % DEFAULT_MODULO  # Modular inverse of the matrix
    np_matrix = np_matrix.astype(int)
    inverse_matrix = []
    for row in np_matrix:
        inverse_matrix.append(list(row))
    return inverse_matrix

def normalise_result_list(result_list: list[int], modulo: int) -> list[int]:
    for i in range(0,len(result_list)):
        result_list[i] = result_list[i] % modulo
    return result_list

def is_valid_character(c):
    if c > 'Z' or c < 'A':
        print(f"Error Invalid character {c}.\nOnly UPPER case characters between a-z allowed in this version.")
        raise f"Invalid Character `{c}` error"
    return

def generate_key_matrix(key: str, length_of_plain_text: int):
    current_index = 0
    key_list_matrix = []
    for _ in range(0,length_of_plain_text):
        current_level_list = []
        for _ in range(0,length_of_plain_text):
            c = key[current_index % len(key)] # to create a n*n sized matrix
            is_valid_character(c)
            current_level_list.append(ord(c) - ord('A'))
            current_index += 1
        key_list_matrix.append(current_level_list)
    return key_list_matrix

def generate_text_list(plain_text: str):
    plain_text_list = []
    for c in plain_text:
      is_valid_character(c) # if false, directly exception is thrown and out of method we go!
      plain_text_list.append(ord(c) - ord('A'))
    return plain_text_list    

def get_string_from_list(result_list: list[int]) -> str:
    result = ""
    for c in result_list:
        result += chr(c + START_VALUE) # since C is already between 0-25; we use A as the start point
    return result


def encrypt(plain_text: str, key: str) -> str:
    plain_text_list = []
    cipher_text = ""
    try:
        plain_text_list = generate_text_list(plain_text)
        key_matrix = generate_key_matrix(key, len(plain_text))
        result_list = matrix_multiply(key_matrix,plain_text_list)
        result_list = normalise_result_list(result_list, DEFAULT_MODULO)
        cipher_text = get_string_from_list(result_list)
    except Exception as e:
        print(e)
        return "-1"    
    return cipher_text

def decrypt(cipher_text: str, key: str) -> str:
    plain_text = ""
    try:
        cipher_text_list = generate_text_list(cipher_text)
        key_matrix = generate_key_matrix(key, len(cipher_text))
        inverse_key_matrix = caculate_inverse_matrix(key_matrix)
        result_list = matrix_multiply(inverse_key_matrix,cipher_text_list)
        result_list = normalise_result_list(result_list, DEFAULT_MODULO)
        plain_text = get_string_from_list(result_list)
    except Exception as e :
        print(e)
        return "-1"
    return plain_text

plain_text = "BRO"
key = "THIS"
cipher_text = encrypt(plain_text, key)
print(f"Cipher Text: {cipher_text}") # should be "POH"
plain_text = decrypt(cipher_text, key)
print(f"Plain Text: {plain_text}")