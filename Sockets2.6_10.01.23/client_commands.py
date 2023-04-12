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

