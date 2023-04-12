import random
import datetime

Digits_Len = 2


def add_len(msg: str) -> bytes:
    zfill_length = str(len(msg)).zfill(Digits_Len)
    return (zfill_length + msg).encode()


def get_len(msg: bytes) -> int:
    msg = msg.decode()
    try:
        return int(msg[:Digits_Len])
    except ValueError:
        return -1


def is_len_valid(length: int) -> bool:
    return length > 0


# def is_cmd_valid(cmd: str) -> bool:
#    return len(cmd) < int("9" * len(cmd))


def TIME() -> str:
    return str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


def WHORU() -> str:
    return "Eitmanushi's Server"


def RAND() -> str:
    return str(random.randint(0, 10))


def Handle_Cmd(cmd: str) -> str:
    if cmd == "TIME":
        msg = TIME()
    elif cmd == "WHORU":
        msg = WHORU()
    elif cmd == "RAND":
        msg = RAND()
    elif cmd == "EXIT":
        msg = "Goodbye :)"
    else:
        msg = "Wrong Protocol"
    return msg
