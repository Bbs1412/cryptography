import socket
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
    s = socket.socket()
    s.connect(("localhost", 6789))

    key = "monarchy".lower()

    cipher_text = s.recv(1024).decode()
    print(f"\n\n[v] `{cipher_text}`")

    plain_text = decipher(cipher_text, key)
    print(f"[~] Deciphered Text : `{plain_text}`")

    print()
    s.close()
