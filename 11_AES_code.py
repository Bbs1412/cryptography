from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def pad(msg):
    padding = 16 - (len(msg) % 16)
    return msg + chr(padding) * padding


def unpad(msg):
    return msg[:-ord(msg[-1])]


def aes_encrypt(msg, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_msg = pad(msg)
    ciphertext = cipher.encrypt(padded_msg.encode())
    return ciphertext


def aes_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext).decode()
    return unpad(decrypted)


if __name__ == "__main__":
    # 128-bit key
    key = get_random_bytes(16)
    # 128-bit IV (initialization vector)
    iv = get_random_bytes(16)

    msg = "Hello AES Secure World"
    ciphertext = aes_encrypt(msg, key, iv)
    print("Encrypted AES:", ciphertext)

    plaintext = aes_decrypt(ciphertext, key, iv)
    print("Decrypted AES:", plaintext)
