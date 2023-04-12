import socket
from protocol import *

input_str = ""

while input_str != "EXIT":
    with socket.socket() as my_socket:
        my_socket.connect(("127.0.0.1", 8820))
        input_str = input("Enter a command: ")
        my_socket.send(add_len(input_str))
        data_len = get_len(my_socket.recv(Digits_Len))  # שדה האורך של הודעת השרת

        if is_len_valid(data_len):  # אם שדה האורך של הודעת השרת תקין
            data = my_socket.recv(data_len).decode()

        else:  # אם שדה האורך של הודעת השרת לר תקין
            data = "Server error"
            my_socket.recv(1024)

        print("The server sent: " + data)
