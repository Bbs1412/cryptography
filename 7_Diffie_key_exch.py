class DiffieHellman:
    def __init__(self, P: int = 23, G: int = 9):
        # Public keys:
        self.public_key = P
        self.generator = G

    def generate_key(self, private_key: int):
        self.private_key = private_key

        # G^a % P
        self.generated_key = pow(
            self.generator, self.private_key, self.public_key)
        return self.generated_key

    def generate_secret(self, exchanged_key: int):
        # exch ^ pvt % P
        self.secret_key = pow(exchanged_key, self.private_key, self.public_key)
        return self.secret_key


if __name__ == "__main__":
    generator = 9
    public_key = 23
    print(f"Public Key \t: {public_key}")
    print(f"Generator \t: {generator}")
    dh = DiffieHellman(P=public_key, G=generator)

    private_key = 4  # 3
    print(f"Private Key \t: {private_key}\n")

    generated_key = dh.generate_key(private_key=private_key)
    print(f"Generated Key \t: {generated_key}")

    # Socket programming to receive the key from other end here:
    exch = 16   # 6
    print(f"Received Key \t: {exch}\n")

    secret_key = dh.generate_secret(exchanged_key=exch)
    print(f"Secret Key \t: {secret_key}")
