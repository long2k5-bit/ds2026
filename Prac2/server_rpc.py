from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import Binary

HOST = "0.0.0.0"
PORT = 8000

def upload_file(name, data):
    """
    Upload a file sent by the client.
    'data' is of type xmlrpc.client.Binary.
    """
    with open(name, "wb") as f:
        f.write(data.data)

    print(f"[+] Received file: {name}")
    return "OK"

# Create and configure the RPC server
server = SimpleXMLRPCServer((HOST, PORT), allow_none=True)
server.register_function(upload_file, "upload_file")

print(f"RPC server running on {HOST}:{PORT} ...")
server.serve_forever()
