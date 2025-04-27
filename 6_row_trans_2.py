def cipher(plain_text, key):
    d, r = divmod(len(plain_text), 4)
    plain_text += "_" * r

    dic = {c: [] for c in key}

    sets = [plain_text[i:i+4] for i in range(0, len(plain_text), 4)]
    for s in sets:
        for i in range(len(key)):
            dic[key[i]].append(s[i])

    ans = ""
    for key in sorted(dic.keys()):
        ans += "".join(dic[key])
    return ans


def decipher(cipher_text, key):
    dic = {c: [] for c in key}
    sets = [cipher_text[i:i+4] for i in range(0, len(cipher_text), 4)]
    keys = [c for c in key]
    sorted_keys = sorted(keys)

    for s, k in zip(sets, sorted_keys):
        dic[k] = s

    ans = ""
    for i in range(len(dic[keys[0]])):
        for ind, k in enumerate(keys):
            ans += dic[k][i]

    return ans[:ans.find("_")]
    # return ans


if __name__ == "__main__":
    print()
    message = "random message".upper()
    key = "nick"
    expected_cipher = "n s_amsedma_roeg".upper()

    print(f"Message \t: `{message}`")
    print(f"Key \t\t: `{key}`")

    cipher_text = cipher(message, key)
    print(f"Cipher  \t: `{cipher_text}`")
    assert cipher_text == expected_cipher

    plain_text = decipher(cipher_text, key)
    print(f"Decipher \t: `{plain_text}`")
    assert plain_text == message

    print("✅ Success")
