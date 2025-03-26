import random
from sympy import mod_inverse


class ElGamal:
    def __init__(self, P: int = 23, G: int = 9):
        self.public_key = P  # Prime number
        self.generator = G  # Generator of the multiplicative group Z*_p

    def generate_keys(self, private_key: int):
        self.private_key = private_key
        self.public_component = pow(
            self.generator, self.private_key, self.public_key)
        return self.public_component  # This is 'h' in ElGamal

    def encrypt(self, M: int, receiver_public: int):
        # Random integer 1 <= k <= p-2
        k = random.randint(1, self.public_key - 2)
        C1 = pow(self.generator, k, self.public_key)
        C2 = (M * pow(receiver_public, k, self.public_key)) % self.public_key
        return C1, C2  # Ciphertext (C1, C2)

    def decrypt(self, C1: int, C2: int):
        s = pow(C1, self.private_key, self.public_key)  # Compute shared secret
        s_inv = mod_inverse(s, self.public_key)  # Compute modular inverse
        M = (C2 * s_inv) % self.public_key  # Recover original message
        return M


if __name__ == "__main__":
    P = 23  # Prime number
    G = 9   # Generator
    elgamal = ElGamal(P, G)

    # Key Generation
    private_key_A = 6  # Alice's private key
    public_key_A = elgamal.generate_keys(private_key_A)
    print(f"Public Key (A) 	: {public_key_A}")

    private_key_B = 15  # Bob's private key
    public_key_B = elgamal.generate_keys(private_key_B)
    print(f"Public Key (B) 	: {public_key_B}")

    # Encryption (Alice encrypts a message for Bob)
    message = 10
    print(f"Original Message 	: {message}")
    C1, C2 = elgamal.encrypt(message, public_key_B)
    print(f"Ciphertext 	: ({C1}, {C2})")

    # Decryption (Bob decrypts the message)
    decrypted_message = elgamal.decrypt(C1, C2)
    print(f"Decrypted Message 	: {decrypted_message}")
