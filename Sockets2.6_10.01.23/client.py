import socket
from typing import Dict, Callable
from client_commands import CLIENT_TIME, CLIENT_RAND, CLIENT_WHORU, CLIENT_EXIT
from exceptions import ExitException

#SERVER_IP = "54.71.128.194"
#SERVER_PORT = 8080
SERVER_IP = "127.0.0.1"
SERVER_PORT = 7107


CLIENT_COMMANDS: Dict[str, Callable[[socket.socket], str]] = \
    {
        "TIME": CLIENT_TIME,
        "RAND": CLIENT_RAND,
        "WHORU": CLIENT_WHORU,
        "EXIT": CLIENT_EXIT,
    }


def get_valid_command() -> str:
    client_command = input("Enter Command: ")
    while client_command not in CLIENT_COMMANDS:
        client_command = input("INVALID COMMAND! Enter Command: ")
    return client_command


def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        while True:
            client_command = get_valid_command()
            command_function = CLIENT_COMMANDS[client_command]
            try:
                command_return = command_function(client_socket)
            except ExitException:
                break
            print(f"The server sent: {command_return}")
        return command_return


if __name__ == "__main__":
    client()
