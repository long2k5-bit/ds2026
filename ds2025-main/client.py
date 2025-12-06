import socket
import os

HOST = "127.0.0.1"
PORT = 5001

filename = input("Enter file to send: ")
filesize = os.path.getsize(filename)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# 1. Send metadata
client.send((filename + "\n").encode())
client.send((str(filesize) + "\n").encode())

# 2. Wait for READY
if client.recv(1024).decode() != "READY":
    client.close()
    raise Exception("Server not ready")

# 3. Send file data
with open(filename, "rb") as f:
    data = f.read(4096)
    while data:
        client.send(data)
        data = f.read(4096)

print("[CLIENT] File sent.")
print(client.recv(1024).decode())

client.close()
