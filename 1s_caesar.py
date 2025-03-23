import socket


def caesar_encipher(message: str, key: int) -> str:
    message = message.upper()

    ans = ""
    a = ord('A')
    for c in message:
        ans += chr((ord(c) - a + key) % 26 + a)
    return ans


if __name__ == "__main__":
    server = socket.socket()
    server.bind(("localhost", 6789))
    server.listen(5)
    client, _ = server.accept()
    print("Connected to client...")

    # plain_text = "ATTACKATONCE"
    # key = 4
    # op = "EXXEGOEXSRGI"

    plain_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = 23
    cipher_text = caesar_encipher(plain_text, key)

    print(f"[^] `{plain_text}`")
    client.send(cipher_text.encode())

    print("\n"*2)
    client.close()
    server.close()

