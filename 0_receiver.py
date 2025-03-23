# This is a receiver which will receive the message from sender
# Receiver will be client side
# socket > connect > s/r 

import socket

s = socket.socket()
server_ip = "localhost"
server_port = 6789

s.connect((server_ip, server_port))
print("\nConnected to server.")

message = "Hello from client"
print(f"\n[^] {message}")
s.send(message.encode())

message = s.recv(1024).decode()
print(f"\n\n[v] {message}")
print()
s.close()


