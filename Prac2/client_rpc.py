import os
from xmlrpc.client import ServerProxy, Binary

SERVER_URL = "http://127.0.0.1:8000/"
FILENAME = "test.txt"  # change this to any file you want to upload


filesize = os.path.getsize(FILENAME)
print(f"Sending {FILENAME} ({filesize} bytes)")

with open(FILENAME, "rb") as f:
    data = f.read()

#take the server proxy (URL) to connect.
proxy = ServerProxy(SERVER_URL, allow_none=True)

#file uploading.
response = proxy.upload_file(FILENAME, Binary(data))

print("Server reply:", response)
