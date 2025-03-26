from Diffie_Hellman import DiffieHellman
import socket

# Connect to server:
serv = socket.socket()
serv.connect(("localhost", 7894))

# Start procedure:
public_key = 23
generator = 9
print(f"Public Key \t: {public_key}")
print(f"Generator \t: {generator}")


dh = DiffieHellman(P=public_key, G=generator)
private_key = 3
print(f"Private Key \t: {private_key}\n")

generated_key = dh.generate_key(private_key=private_key)
print(f"Generated Key \t: {generated_key}\n")

serv.send(str(generated_key).encode())
print(f"[^] Sent my Key  : {generated_key}")

exch = serv.recv(1024).decode()
exch = int(exch)
print(f"\n\n[v] Received Key : {exch}\n")

secret_key = dh.generate_secret(exchanged_key=exch)
print(f"Secret Key \t: {secret_key}")

serv.close()