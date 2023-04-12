from socket import socket, AF_INET, SOCK_STREAM


my_socket = socket(AF_INET, SOCK_STREAM)
my_socket.connect(("10.100.102.56", 8820))
my_socket.send("Eitam".encode())
data = my_socket.recv(1024).decode()
print("The server sent " + data)
my_socket.close()