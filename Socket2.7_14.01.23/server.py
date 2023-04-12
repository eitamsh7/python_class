import socket
from server_commands import SERVER_TIME, SERVER_RAND, SERVER_WHORU, SERVER_EXIT, SERVER_DIR, SERVER_DELETE, SERVER_COPY, \
    SERVER_EXECUTE, SERVER_TAKE_SCREENSHOT
from utils import recv_message, send_message
from typing import Dict
from exceptions import ExitException

SERVER_LISTEN_IP = "0.0.0.0"
SERVER_LISTEN_PORT = 7107

SERVER_COMMANDS: Dict = \
    {
        "TIME": SERVER_TIME,
        "RAND": SERVER_RAND,
        "WHORU": SERVER_WHORU,
        "EXIT": SERVER_EXIT,
    }

SERVER_NEW_COMMANDS: Dict = \
    {
        "DIR": SERVER_DIR,
        "DELETE": SERVER_DELETE,
        "COPY": SERVER_COPY,
        "EXECUTE": SERVER_EXECUTE,
        "TAKE_SCREENSHOT": SERVER_TAKE_SCREENSHOT

    }


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:  # AF_INT = internet, SOCK_STREAM = TCP
        server_socket.bind((SERVER_LISTEN_IP, SERVER_LISTEN_PORT))
        server_socket.listen()
        while True:
            (client_socket, client_address) = server_socket.accept()
            while True:
                client_command = recv_message(client_socket)
                client_new_command_only = client_command.split()[0]
                if client_new_command_only in SERVER_NEW_COMMANDS:
                    handle_function = SERVER_NEW_COMMANDS[client_new_command_only]
                    if client_new_command_only == "COPY":
                        folder_copy_name = client_command.split()[1]
                        folder_paste_name = client_command.split()[2]
                        try:
                            response = handle_function(folder_copy_name, folder_paste_name)
                        except Exception as err:
                            response = str(err)
                    else:
                        folder_name = client_command.split()[1]
                        try:
                            response = handle_function(folder_name)
                        except Exception as err:
                            response = str(err)
                else:
                    handle_function = SERVER_COMMANDS[client_command]
                    try:
                        response = handle_function()
                    except ExitException:
                        client_socket.close()
                        break
                send_message(response, client_socket)


if __name__ == "__main__":
    server()
