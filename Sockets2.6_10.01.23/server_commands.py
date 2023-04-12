import datetime
import random
from exceptions import ExitException


def SERVER_TIME() -> str:
    return datetime.datetime.now().strftime("The time is: %d/%m/%Y, %H:%M:%S")


def SERVER_RAND() -> str:
    return str(random.randint(0, 10000))


def SERVER_WHORU() -> str:
    return "Eitmanushi's Server"


def SERVER_EXIT() -> str:
    raise ExitException("RECEIVED EXIT COMMAND!")


