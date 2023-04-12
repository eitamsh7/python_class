import socket
from Server_Commands import *

SERVER_LISTEN_IP = "0.0.0.0"
SERVER_LISTEN_PORT = 1337


def send_msg(msg: str, client_socket: socket):
    msg_data = msg.encode()
    client_socket.send(msg_data)


def server():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((SERVER_LISTEN_IP, SERVER_LISTEN_PORT))
            server_socket.listen()
            (client_socket, client_address) = server_socket.accept()
            time = SERVER_TIME()
            NEW_SERVER_LISTEN_PORT = SERVER_RAND()
            send_msg(str(NEW_SERVER_LISTEN_PORT), client_socket)
            client_socket.close()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((SERVER_LISTEN_IP, NEW_SERVER_LISTEN_PORT))
            server_socket.listen()
            (client_socket, client_address) = server_socket.accept()
            send_msg(time, client_socket)
            client_socket.close()


if __name__ == "__main__":
    server()
