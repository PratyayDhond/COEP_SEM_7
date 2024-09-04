DEFAULT_MODULO = 26
START_VALUE = 65

def matrix_multiply(key_matrix: list[int], text_matrix: list[int]) -> str:
    n = len(key_matrix)
    result_vector = [0] * n
    for i in range(n):
        for j in range(n):
            result_vector[i] += key_matrix[i][j] * text_matrix[j]
    
    return result_vector

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
    # print(plain_text_list)
    
    return cipher_text
    pass

def decrypt(cipher_text: str, key: str) -> str:
    pass



cipher_text = encrypt("ACT", "GYBNQKURP")
print(cipher_text) # should be "POH"
plain_text = decrypt()
