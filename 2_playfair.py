# Steps:
# Create 5x5 matrix from the key
# Diagraphs of the plainText
# 1. If both chars same, add filler 'x'
# 2. If odd no of chars, add one 'z' in the end.
# Encrypt:
# 1. If both in same col, take chars below them from matrix.
# 2. If both in same row, take chars right to them from matrix.
# 3. Else, take opposite corners of the rectangle formed

from typing import List


def create_matrix(key: str) -> List[List[str]]:
    alphabets = []

    for c in key:
        if c not in alphabets:
            alphabets.append(c)

    for i in range(ord('a'), ord('z') + 1):
        char = chr(i)
        if char not in alphabets and char != 'j':
            alphabets.append(chr(i))

    # Form 5x5 matrix:
    matrix = [["j" for _ in range(5)] for __ in range(5)]

    ind = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = alphabets[ind]
            ind += 1

    # print(alphabets)
    # print("", *matrix, sep="\n\t")
    return matrix


def create_diagraphs(plain_text: str) -> List[List[str]]:
    i = 0
    dia = []

    while (i < len(plain_text) and i+1 < len(plain_text)):
        a, b = plain_text[i], plain_text[i+1]

        # Add filler char 'x' if both are same:
        if a == b:
            b = 'x'
            i += 1
        else:
            i += 2

        dia.append([a, b])

    # Add 'z' in end if odd length str (last one is alone)
    if i == len(plain_text) - 1:
        dia.append([plain_text[i], 'z'])

    # print(dia)
    return dia


def get_row_col(char: str, matrix: List[List[str]]):
    """Iterate over entire matrix to return the row and col numbers of given character in the matrix"""
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)
    return (-1, -1)


def encrypt(diagraph: List[str], matrix: List[List[str]]) -> List[str]:
    a, b = diagraph
    a_row, a_col = get_row_col(a, matrix)
    b_row, b_col = get_row_col(b, matrix)

    # If in same col:
    if a_col == b_col:
        return [matrix[(a_row + 1) % 5][a_col], matrix[(b_row + 1) % 5][b_col]]
    # If in same row:
    elif a_row == b_row:
        return [matrix[a_row][(a_col + 1) % 5], matrix[b_row][(b_col + 1) % 5]]
    # Else rectangle rule:
    else:
        return [matrix[a_row][b_col], matrix[b_row][a_col]]


def cipher(plain_text: str, key: str) -> str:
    # Create matrix:
    matrix = create_matrix(key)

    # Create diagraphs:
    dia = create_diagraphs(plain_text)

    # Encipher:
    cipher_text = ""

    for d in dia:
        cipher_text += "".join(encrypt(d, matrix))

    return cipher_text


def decrypt(diagraph: List[str], matrix: List[List[str]]) -> List[str]:
    a, b = diagraph
    a_row, a_col = get_row_col(a, matrix)
    b_row, b_col = get_row_col(b, matrix)

    # If in same col:
    if a_col == b_col:
        return [matrix[(a_row - 1) % 5][a_col], matrix[(b_row - 1) % 5][b_col]]
    # If in same row:
    elif a_row == b_row:
        return [matrix[a_row][(a_col - 1) % 5], matrix[b_row][(b_col - 1) % 5]]
    # Else rectangle rule:
    else:
        return [matrix[a_row][b_col], matrix[b_row][a_col]]


def decipher(cipher_text: str, key: str) -> str:
    # Create matrix:
    matrix = create_matrix(key)

    # Create diagraphs:
    dia = create_diagraphs(cipher_text)

    # Decipher:
    plain_text = ""

    for d in dia:
        a, b = decrypt(d, matrix)

        if b == 'x':
            plain_text += a
        else:
            plain_text += a
            plain_text += b

    return plain_text


if __name__ == "__main__":
    key = "monarchy".lower()
    message = "hello"

    # Create matrix:
    # matrix = create_matrix(key)

    # Create diagraphs:
    # dia = create_diagraphs("hello")
    # print(dia)

    # Check the encryption:
    # item = ["m", "e"]         # ["c", "l"]
    # item = ["s", "t"]         # ["t", "l"]
    # item = ["n", "t"]         # ["r", "q"]
    # print(item, encrypt(item, matrix))

    cipher_text = cipher(message, key)
    print(cipher_text)

    # Check the decryption:
    # item = ["c", "l"]           # ["m", "e"]
    # item = ["t", "l"]           # ["s", "t"]
    # item = ["r", "q"]           # ["n", "t"]
    # print(item, decrypt(item, matrix))

    plain_text = decipher(cipher_text, key)
    print(plain_text)
