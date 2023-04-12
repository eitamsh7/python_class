import socket
from protocol import *


def server():
    while True:
        with socket.socket() as server_socket:
            server_socket.bind(("0.0.0.0", 8820))
            server_socket.listen()
            (client_socket, client_address) = server_socket.accept()
            with client_socket as client_socket:
                data_len = get_len(client_socket.recv(Digits_Len))  # שדה האורך של הודעת הלקוח
                data = ""

                if is_len_valid(data_len):  # אם אורך שדה הודעת הלקוח תקין
                    data = client_socket.recv(data_len).decode()
                    msg = Handle_Cmd(data)

                else:  # אם אורך שדה הודעת הלקוח לא תקין
                    data = "Wrong Protocol"
                    server_socket.recv(1024)

                client_socket.send(add_len(msg))
                if data == "EXIT":
                    break


server()
