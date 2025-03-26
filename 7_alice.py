from Diffie_Hellman import DiffieHellman
import socket

# Create server:
s = socket.socket()
s.bind(("", 7894))
s.listen(5)

# Get connections:
client, _ = s.accept()

# Start procedure:
public_key = 23
generator = 9
print(f"Public Key \t: {public_key}")
print(f"Generator \t: {generator}")


dh = DiffieHellman(P=public_key, G=generator)
private_key = 4
print(f"Private Key \t: {private_key}\n")

generated_key = dh.generate_key(private_key=private_key)
print(f"Generated Key \t: {generated_key}\n")

exch = client.recv(1024).decode()
exch = int(exch)
print(f"\n[v] Received Key : {exch}")

client.send(str(generated_key).encode())
print(f"[^] Sent my Key  : {generated_key}\n\n")

secret_key = dh.generate_secret(exchanged_key=exch)
print(f"Secret Key \t: {secret_key}")

s.close()
