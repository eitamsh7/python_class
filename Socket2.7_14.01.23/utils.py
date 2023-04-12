import socket
from exceptions import InvalidMessage

MESSAGE_LEN_LENGTH = 4


def encode_message(message: str) -> bytes:
    message_bytes = message
    message_bytes_len = str(len(message_bytes)).zfill(MESSAGE_LEN_LENGTH)
    return message_bytes_len.encode() + message_bytes.encode()


def decode_message_len(data: bytes) -> int:
    try:
        temp = data[:MESSAGE_LEN_LENGTH]
        message_bytes_len = int(temp)
    except ValueError:
        raise InvalidMessage("THE LEN FIELD DOESN'T ONLY CONTAIN NUMBERS!")
    return message_bytes_len


def decode_message(message_len: int, data: bytes) -> str:
    message_bytes = data
    if len(data) != message_len:
        raise InvalidMessage("THE LEN FIELD DOESN'T FIT THE MESSAGE!")
    return message_bytes.decode()


def send_message(message: str, client_socket: socket):
    message_data = encode_message(message)
    client_socket.send(message_data)


def recv_message(client_socket: socket) -> str:
    message_len_bytes = client_socket.recv(MESSAGE_LEN_LENGTH)
    message_len = decode_message_len(message_len_bytes)
    message_bytes = client_socket.recv(message_len)
    message = decode_message(message_len, message_bytes)
    return message
