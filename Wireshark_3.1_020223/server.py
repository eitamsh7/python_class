from socket import socket, AF_INET, SOCK_STREAM


server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen()
print("Server is up and running")
while True:
    (client_socket, client_address) = server_socket.accept()
    print("\nCLIENT CONNECTED")
    data = client_socket.recv(1024).decode()
    print(">>>> Client sent: " + data)
    reply = "Hello " + data
    client_socket.send(reply.encode())

client_socket.close()
server_socket.close()