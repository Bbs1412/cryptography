import numpy as np

alphabets = [chr(i) for i in range(65, 91)]
mappings = {char: ord(char)-ord('A') for char in alphabets}
# inv_mappings = {val: key for (key, val) in mappings.items()}
inv_mappings = {ind: char for ind, char in enumerate(alphabets)}

# print(mappings)
# print(inv_mappings)


def matrix_inverse(matrix, mod=26):
    """Computes the modular inverse of a 3x3 matrix under mod."""

    # Compute the determinant of the matrix
    det = int(round(np.linalg.det(matrix)))

    # Compute the modular inverse of the determinant under mod (not int)
    det_inv = pow(det, -1, mod)

    # Compute the adjugate (adjoint) of the matrix
    invert = np.linalg.inv(matrix)
    adjoint = np.round(det * invert).astype(int)

    # Compute the modular inverse matrix
    matrix_inv = (det_inv * adjoint) % mod

    return matrix_inv


def encrypt(plain_text: str, key):
    message = plain_text
    message = message.upper()

    ans = ""

    if len(message) % 3 != 0:
        q, rem = divmod(len(message), 3)
        message += "Z" * (rem + 1)

    # print(message, len(message))

    for i in range(0, len(message), 3):
        block = message[i:i+3]
        mapped = [mappings[c] for c in block]
        prod = np.dot(key, mapped) % 26
        # prod = prod.flatten().tolist()[0]
        prod = prod.reshape((3,)).tolist()[0]

        ans += "".join([inv_mappings[c] for c in prod])
    return ans


def decrypt(cipher_text, key):
    ans = ""
    # assuming that message is already in multiple of three:
    for i in range(0, len(cipher_text), 3):
        block = [mappings[c] for c in cipher_text[i:i+3]]
        # print(block)
        prod = np.dot(key, block) % 26
        prod = prod.reshape(3, ).tolist()[0]

        ans += "".join([inv_mappings[n] for n in prod])
    return ans


if __name__ == "__main__":
    key = "GYBNQKURP"

    key_nums = [mappings[c] for c in key]
    key_nums = np.matrix(key_nums).reshape((3, 3))
    inv_key = matrix_inverse(key_nums)

    print(key_nums)
    print(inv_key)

    message = "HelloWorld"
    print(f"Key \t\t: {key}")
    print(f"Message \t: {message}")

    cipher = encrypt(message, key_nums)
    print(f"Cipher  \t: {cipher}")

    decipher = decrypt(cipher, inv_key)
    print(f"Decipher \t: {decipher}")
