import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))  # Bind to all network interfaces
server.listen(5)
print("Server listening on port 12345...")

conn, addr = server.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == "exit":
        print("Connection closed.")
        break
    print(f"Client: {data}")
    conn.sendall(input("Reply: ").encode())

conn.close()
server.close()
