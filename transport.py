import socket

def start_transport_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8080))
    server.listen(1)
    print("[Layer 4] TCP Server listening on 127.0.0.1:8080")
    
    conn, addr = server.accept()
    print(f"[Layer 4] Connection from {addr}")
    conn.sendall(b"Hello from Transport Layer!")
    conn.close()

if __name__ == "__main__":
    start_transport_server()
