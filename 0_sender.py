# This is a sender which will send the message to receiver
# Sender will be server side
# socket > bind > listen > accept > s/r

import socket

s = socket.socket()
address = ''
port = 6789
s.bind((address, port))
s.listen(5)
print("Server listening...")

client, addr = s.accept()
print(f"Connected successfully...")

message = client.recv(1024).decode()
print(f"\n\n[v] {message}")

message = "Thank you for connection!!"
client.send(message.encode())
print(f"[^] {message}")
print()

client.close()
s.close()