alpha = [chr(i) for i in range(65, 91)]
maps = {char: ind for ind, char in enumerate(alpha)}
inv_maps = {val: key for key, val in maps.items()}


def match_key_len(key, need_len):
    mul, rem = divmod(need_len, len(key))
    key = key * mul
    key += key[0:rem]
    return key


def encrypt(plain_text: str, key: str):
    plain_text = plain_text.upper()
    ans = ""
    extended_key = match_key_len(key, len(plain_text))

    for c_msg, c_key in zip(plain_text, extended_key):
        ans += inv_maps[(maps[c_msg] + maps[c_key]) % 26]
    return ans


def decrypt(cipher_text: str, key: str):
    ans = ""
    extended_key = match_key_len(key, len(cipher_text))

    for c_msg, c_key in zip(cipher_text, extended_key):
        ans += inv_maps[(maps[c_msg] - maps[c_key] + 26) % 26]
    return ans


if __name__ == "__main__":
    # print(match_key("abc", 8))
    key = "AYUSH"
    message = "GEEKSFORGEEKS"

    print(f"Key \t\t: {key}")
    print(f"Message \t: {message}")

    cipher = encrypt(message, key)
    print(f"Cipher  \t: {cipher}")

    decipher = decrypt(cipher, key)
    print(f"Decipher \t: {decipher}")
