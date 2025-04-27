from typing import List


def caesar_decipher(cipher_text: str, shift: int) -> str:
    cipher_text = cipher_text.upper()

    ans = ""
    a = ord('A')
    for c in cipher_text:
        ans += chr((ord(c) - a - shift) % 26 + a)
    return ans


def caesar_decipher_with_keyword(cipher_text: str, keyword: str) -> List[int]:
    cipher_text = cipher_text.upper()

    answers = {}
    a = ord('A')

    for shift in range(0, 26):
        ans = ""
        for c in cipher_text:
            ans += chr((ord(c) - a - shift) % 26 + a)

        if keyword.upper() in ans:
            answers[shift] = ans

    return answers


if __name__ == "__main__":
    word = "UVACLYFZLJBYL"

    # Without keyword
    de_ciphered = caesar_decipher(word, 2)
    print(de_ciphered)

    # With keyword
    answers = caesar_decipher_with_keyword(word, "ob")
    print("ob     ->", answers)

    answers = caesar_decipher_with_keyword(word, "secure")
    print("secure ->", answers)
