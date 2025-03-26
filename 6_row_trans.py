alpha = [chr(i) for i in range(65, 91)]
maps = {char: ind for ind, char in enumerate(alpha)}
inv_maps = {val: key for key, val in maps.items()}


def encrypt(plain_text: str, key: str) -> str:
    answer = ""
    dic = {}

    # Add fillers to create even sized blocks:
    if len(plain_text) % len(key) != 0:
        plain_text += "_" * (len(key) - (len(plain_text) % len(key)))

    temp = ["" for _ in range(len(key))]
    ind = 0

    for char in plain_text:
        temp[ind] += char
        ind = (ind + 1) % len(key)

    for ind, char in enumerate(key):
        dic[char] = temp[ind]

    keys: list = list(dic.keys())
    # print(keys)
    for k in sorted(keys):
        answer += dic[k]

    return answer


def decrypt(cipher_text: str, key: str) -> str:
    ans = ""
    dic = {}

    temp = []
    keys = [k for k in key]
    block_size = len(cipher_text) // len(key)

    for i, c in enumerate(sorted(keys)):
        dic[c] = cipher_text[i*block_size: (i+1)*block_size]

    for j in range(block_size):
        for k in keys:
            ans += dic[k][j]

    return ans


if __name__ == "__main__":
    # print(match_key("abc", 8))
    key = "HACK"
    message = "Geeks for Geeks"
    # "e  kefGsGsrekoe_"

    print(f"Key \t\t: {key}")
    print(f"Message \t: {message}")

    cipher = encrypt(message, key)
    print(f"Cipher  \t: {cipher}")

    decipher = decrypt(cipher, key)
    print(f"Decipher \t: {decipher}")
