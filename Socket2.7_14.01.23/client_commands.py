from socket import socket
from utils import send_message, recv_message
from exceptions import ExitException


def CLIENT_TIME(client_socket: socket) -> str:
    send_message("TIME", client_socket)
    response = recv_message(client_socket)
    return response


def CLIENT_RAND(client_socket: socket) -> str:
    send_message("RAND", client_socket)
    response = recv_message(client_socket)
    return response


def CLIENT_WHORU(client_socket: socket) -> str:
    send_message("WHORU", client_socket)
    response = recv_message(client_socket)
    return response


def CLIENT_EXIT(client_socket: socket) -> str:
    send_message("EXIT", client_socket)
    raise ExitException("CONNECTION END BY THE CLIENT!")


def CLIENT_DIR(client_socket: socket, dir_folder_name: str) -> str:
    send_message(f"DIR {dir_folder_name}", client_socket)
    response = recv_message(client_socket)
    return response


def CLIENT_DELETE(client_socket: socket, delete_folder_name: str) -> str:
    send_message(f"DELETE {delete_folder_name}", client_socket)
    response = recv_message(client_socket)
    return response


def CLIENT_COPY(client_socket: socket, copy_folder_name: str, paste_folder_name: str) -> str:
    send_message(f"COPY {copy_folder_name} {paste_folder_name}", client_socket)
    response = recv_message(client_socket)
    return response


def CLIENT_EXECUTE(client_socket: socket, execute_folder_name: str) -> str:
    send_message(f"EXECUTE {execute_folder_name}", client_socket)
    response = recv_message(client_socket)
    return response


def CLIENT_TAKE_SCREENSHOT(client_socket: socket, take_screenshot_folder_name: str) -> str:
    send_message(f"TAKE_SCREENSHOT {take_screenshot_folder_name}", client_socket)
    response = recv_message(client_socket)
    return response


