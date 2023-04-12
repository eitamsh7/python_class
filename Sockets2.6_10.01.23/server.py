import socket
from server_commands import SERVER_TIME, SERVER_RAND, SERVER_WHORU, SERVER_EXIT
from utils import recv_message, send_message
from typing import Dict, Callable
from exceptions import ExitException

SERVER_LISTEN_IP = "0.0.0.0"
SERVER_LISTEN_PORT = 7107

SERVER_COMMANDS: Dict[str, Callable[[], str]] = \
    {
        "TIME": SERVER_TIME,
        "RAND": SERVER_RAND,
        "WHORU": SERVER_WHORU,
        "EXIT": SERVER_EXIT,
    }


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:  # AF_INT = internet, SOCK_STREAM = TCP
        server_socket.bind((SERVER_LISTEN_IP, SERVER_LISTEN_PORT))
        server_socket.listen()
        while True:
            (client_socket, client_address) = server_socket.accept()
            while True:
                client_command = recv_message(client_socket)
                handle_function = SERVER_COMMANDS[client_command]
                try:
                    response = handle_function()
                except ExitException:
                    client_socket.close()
                    break
                send_message(response, client_socket)


if __name__ == "__main__":
    server()
