import socket
from typing import Dict
from client_commands import CLIENT_TIME, CLIENT_RAND, CLIENT_WHORU, CLIENT_EXIT, CLIENT_DIR, CLIENT_DELETE, CLIENT_COPY, \
    CLIENT_EXECUTE, CLIENT_TAKE_SCREENSHOT
from exceptions import ExitException

SERVER_IP = "127.0.0.1"
SERVER_PORT = 7107

CLIENT_COMMANDS: Dict = \
    {
        "TIME": CLIENT_TIME,
        "RAND": CLIENT_RAND,
        "WHORU": CLIENT_WHORU,
        "EXIT": CLIENT_EXIT,
    }

CLIENT_NEW_COMMANDS: Dict = \
    {
        "DIR": CLIENT_DIR,
        "DELETE": CLIENT_DELETE,
        "COPY": CLIENT_COPY,
        "EXECUTE": CLIENT_EXECUTE,
        "TAKE_SCREENSHOT": CLIENT_TAKE_SCREENSHOT
    }


def get_valid_command() -> str:
    client_command = input("Enter Command: ")
    while client_command not in CLIENT_COMMANDS and client_command not in CLIENT_NEW_COMMANDS:
        client_command = input("INVALID COMMAND! Enter Command: ")
    return client_command


def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        while True:
            client_command = get_valid_command()
            if client_command in CLIENT_NEW_COMMANDS:
                if client_command == "COPY":
                    folder_copy_name = input("Enter folder name to copy: ")
                    folder_paste_name = input("Enter folder name to paste : ")
                    command_function = CLIENT_NEW_COMMANDS[client_command]
                    try:
                        command_return = command_function(client_socket, folder_copy_name, folder_paste_name)
                    except Exception as err:
                        command_return = str(err)
                else:
                    folder_name = input("Enter folder name: ")
                    command_function = CLIENT_NEW_COMMANDS[client_command]
                    try:
                        command_return = command_function(client_socket, folder_name)
                    except Exception as err:
                        command_return = str(err)
            else:
                command_function = CLIENT_COMMANDS[client_command]
                try:
                    command_return = command_function(client_socket)
                except ExitException:
                    break
            print(f"The server sent: {command_return}")
        return command_return


if __name__ == "__main__":
    client()
