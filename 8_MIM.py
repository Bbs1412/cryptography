from Crypto.Cipher import AES

iv = b'0123456789abcdef'


def generate_public_key(private_key, alpha, p):
    return pow(alpha, private_key, p) % (2**128)


def generate_common_key(private_key, public_key, p):
    return pow(public_key, private_key, p) % (2**128)


def pad(msg):
    padding_len = 16 - (len(msg) % 16)
    return msg + "-" * padding_len


def encryption(msg, key):
    bytes_key = key.to_bytes(16, byteorder="big")
    padded_msg = pad(msg)
    bytes_msg = padded_msg.encode('utf-8')
    cipher = AES.new(bytes_key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(bytes_msg)
    return ciphertext


def decryption(ciphertext, key):
    bytes_key = key.to_bytes(16, byteorder="big")
    cipher = AES.new(bytes_key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('utf-8').rstrip('-')


def x_send_msg_to_y(ck):
    msg = "i have 200k in my account."
    ciphertext = encryption(msg, ck)
    response = send(ciphertext, ck)
    plaintext = decryption(response, ck)

    print(f"------------------------X-side-of-story----------------------------")
    print(f"msg_send: {msg}")
    print(f"response_from_y: {plaintext}\n\n")


def y_receive_wrong_msg(ck):
    response = receive(ck)
    plaintext = decryption(response, ck)

    print(f"--------------------------Y-side-of-story---------------------------")
    print(f"msg_received: {plaintext}")


def send(ciphertext, ck_x):
    plaintext = decryption(ciphertext, ck_x)
    msg = "send me xxx amount on account no: xxxxxxx"
    ciphertext = encryption(msg, ck_x)
    return ciphertext


def receive(ck_y):
    msg = "i need xxx amount, send me on account no: xxxxx"
    ciphertext = encryption(msg, ck_y)
    return ciphertext


if __name__ == "__main__":
    p = 23
    alpha = 5
    xa = 6
    ya = 15
    z_x = 12
    z_y = 9
    xpk = generate_public_key(xa, alpha, p)
    ypk = generate_public_key(ya, alpha, p)
    zpk_x = generate_public_key(z_x, xpk, p)
    zpk_y = generate_public_key(z_y, ypk, p)
    ck_z_x = generate_common_key(zpk_x, z_x, p)
    ck_z_y = generate_common_key(zpk_y, z_y, p)
    # man_in_middle(ck_z_x, ck_z_y)
    x_send_msg_to_y(ck_z_x)
    y_receive_wrong_msg(ck_z_y)
