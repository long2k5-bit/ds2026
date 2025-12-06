import socket

HOST = "0.0.0.0"
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("[SERVER] Waiting for client...")

conn, addr = server.accept()
print(f"[SERVER] Connected by {addr}")

# 1. Receive filename
filename = conn.recv(1024).decode().strip()
print("[SERVER] Filename:", filename)

# 2. Receive filesize
filesize = int(conn.recv(1024).decode().strip())
print("[SERVER] Filesize:", filesize)

conn.send(b"READY")

# 3. Receive file data
with open(filename, "wb") as f:
    received = 0
    while received < filesize:
        data = conn.recv(4096)
        if not data:
            break
        f.write(data)
        received += len(data)

print("[SERVER] File received successfully.")
conn.send(b"OK")
conn.close()
