import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "127.0.0.1"  # Replace with the actual public IP
client.connect((server_ip, 12345))

while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break
    client.sendall(msg.encode())
    print("Server:", client.recv(1024).decode())

client.close()
