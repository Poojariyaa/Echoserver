import socket
HOST = "127.0.0.1"
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) 
    s.sendall(b"Pooja V,")
    s.sendall(b"212221040122")
    data = s.recv(1024)
print(f"\nRecived {data!r}")