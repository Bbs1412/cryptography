import socket


def caesar_decipher(cipher_text: str, shift: int) -> str:
    cipher_text = cipher_text.upper()

    ans = ""
    a = ord('A')
    for c in cipher_text:
        ans += chr((ord(c) - a - key) % 26 + a)
    return ans


if __name__ == "__main__":
    s = socket.socket()
    s.connect(("localhost", 6789))

    cipher_text = s.recv(1024).decode()
    print(f"\n\n[v] `{cipher_text}`")

    key = 23
    plain_text = caesar_decipher(cipher_text, 4)
    print(f"[~] Deciphered Text : `{plain_text}`")

    print()
    s.close()
