import datetime
import random
from time import sleep
from exceptions import ExitException
import glob
import os
import shutil
import subprocess
import pyautogui


def SERVER_TIME() -> str:
    return datetime.datetime.now().strftime("The time is: %d/%m/%Y, %H:%M:%S")


def SERVER_RAND() -> str:
    return str(random.randint(0, 10000))


def SERVER_WHORU() -> str:
    return "Eitmanushi's Server"


def SERVER_EXIT() -> str:
    raise ExitException("RECEIVED EXIT COMMAND!")


def SERVER_DIR(dir_folder_name: str) -> str:
    folder = dir_folder_name + r'\*.*'
    files_list = glob.glob(folder)
    return str(files_list)


def SERVER_DELETE(delete_folder_name: str) -> str:
    os.remove(delete_folder_name)
    return f"{delete_folder_name} Deleted succeed!"


def SERVER_COPY(copy_folder_name: str, paste_folder_name: str) -> str:
    shutil.copy(copy_folder_name, paste_folder_name)
    return f"{copy_folder_name} copied, and pasted in {paste_folder_name} successfully!"


def SERVER_EXECUTE(execute_folder_name: str) -> str:
    subprocess.call(execute_folder_name)
    return f"The application {execute_folder_name} has been run successfully!"


def SERVER_TAKE_SCREENSHOT(take_screenshot_folder_name: str) -> str:
    #sleep(5)
    image = pyautogui.screenshot()
    image.save(take_screenshot_folder_name)
    return f"The screenshot has been already taken! It is saved in {take_screenshot_folder_name}!"
