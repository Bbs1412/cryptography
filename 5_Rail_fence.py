def encrypt(plain_text: str, rails: int) -> str:
    ans = ["" for i in range(rails)]
    direction_up = False
    ind = 0

    for i in range(0, len(plain_text)):
        ans[ind] += plain_text[i]

        # Get next rail index:
        if direction_up:
            ind = (ind - 1) % rails
        else:
            ind = (ind + 1) % rails

        # Change dir on extremes:
        if ind == rails - 1 or ind == 0:
            direction_up = not direction_up

    return "".join(ans)


def decrypt(cipher_text: str, rails: int) -> str:
    # Create placeholder answer of exact length:
    answer = [" " for _ in range(len(cipher_text))]

    # hard code for n == 3, i dont have time to generalise the formulas
    # Go and check the leet-codes i have done so far, in Zig Zag question,
    # I already have generalized the pattern calc

    # Or, copy the same encryption loops here, and instead of chars
    # append in the indices in sub arrays in one common array
    # Thus, by using same enc code, we get indices
    # And finally, just use those indices from merged array

    first, sec, third = [], [], []

    i = 0
    while (i < len(cipher_text)):
        first.append(i)
        i += 4

    i = 1
    while (i < len(cipher_text)):
        sec.append(i)
        i += 2

    i = 2
    while (i < len(cipher_text)):
        third.append(i)
        i += 4

    merged = first + sec + third

    for i, c in enumerate(cipher_text):
        answer[merged[i]] = c

    return "".join(answer)


if __name__ == "__main__":
    # print(match_key("abc", 8))
    rails = 3
    message = "defend the east wall"
    # "dnhaweedtees alf  tl"
    # message = "i am the one here"

    print(f"Rails \t\t: {rails}")
    print(f"Message \t: {message}")

    cipher = encrypt(message, rails)
    print(f"Cipher  \t: {cipher}")

    decipher = decrypt(cipher, rails)
    print(f"Decipher \t: {decipher}")
