import math


class RSA:
    def __init__(self, p: int, q: int):
        self.p = p
        self.q = q
        self.n = p*q
        self.phi = (self.p-1) * (self.q-1)

    def generate_enc_expo(self):
        phi = self.phi

        # co prime e such that [ 1 < e < phi ]
        for i in range(2, phi):
            if math.gcd(i, phi) == 1:
                self.e = i
                break

        return self.e

    def generate_dec_expo(self):
        # for d in range(2, self.phi, ):
        for d in range(self.phi, 2, -1):
            if self.e*d % self.phi == 1:
                self.d = d
                break
        return self.d

        # self.d = pow(self.e, -1, self.phi)
        # return self.d

    def encrypt(self, message: int, public_key: int) -> int:
        return pow(message, public_key, self.n)

    def decrypt(self, message: int) -> int:
        return pow(message, self.d, self.n)


if __name__ == "__main__":
    p = 7919
    q = 1009
    print(f"Prime P \t: {p}")
    print(f"Prime Q \t: {q}")

    rsa = RSA(p, q)
    print(f"Modulus N \t: {rsa.n}")
    print(f"Phi \t\t: {rsa.phi}")

    e = rsa.generate_enc_expo()
    print(f"\nPublic Key E \t: {e}")

    d = rsa.generate_dec_expo()
    print(f"Private Key D \t: {d}")

    message = 1234
    print(f"\nMessage \t: {message}")

    encrypted_message = rsa.encrypt(message, e)
    print(f"Encrypted \t: {encrypted_message}")

    decrypted_message = rsa.decrypt(encrypted_message)
    print(f"Decrypted \t: {decrypted_message}")

    assert message == decrypted_message, "Decryption failed!"
    print("Decryption successful!")
