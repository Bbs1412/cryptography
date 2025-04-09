from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes


def pad(msg):
    padding = 8 - (len(msg) % 8)
    return msg + chr(padding) * padding


def unpad(msg):
    return msg[:-ord(msg[-1])]


def des_encrypt(msg, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_msg = pad(msg)
    ciphertext = cipher.encrypt(padded_msg.encode())
    return ciphertext


def des_decrypt(ciphertext, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext).decode()
    return unpad(decrypted)


if __name__ == "__main__":
    # 64-bit key
    key = get_random_bytes(8)
    # 64-bit IV (initialization vector)
    iv = get_random_bytes(8)

    msg = "Hello DES Secure World"
    ciphertext = des_encrypt(msg, key, iv)
    print("Encrypted DES:", ciphertext)

    plaintext = des_decrypt(ciphertext, key, iv)
    print("Decrypted DES:", plaintext)
