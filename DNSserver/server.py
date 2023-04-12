import socket

SNS_SERVERIP = "0.0.0.0"
DNS_SERVER_PORT = 53
DEFAULT_BUFFER_SIZE = 1024


def dns_handler(data: bytes):
    new_ip = '212.143.70.40'
    packet_flags: bytes = b"\x81\x83"
    packet_question: bytes = b"\x00\x01"
    packet_answers_rrs: bytes = b"\x00\x00"
    packet_authority_rrs: bytes = b"\x00\x00"
    packet_additional_rrs: bytes = b"\x00\x00"
    packet_name: bytes = data[12:data.find(b"\x00", 12) + 1]
    packet_name_length: bytes = hex(len(packet_name)).encode()
    packet_label_count: bytes = b"\x00\x02"
    packet_type: bytes = b"\x00\x1C"
    packet_class: bytes = b"\x00\x01"
    packet_data_len: bytes = bytes(len(data))
    packet_ip_bytes: bytes = bytes([int(byte) for byte in new_ip.split(".")])
    new_packet = packet_flags + packet_question + packet_answers_rrs + packet_authority_rrs \
                 + packet_additional_rrs + packet_name + packet_name_length + packet_label_count + packet_type \
                 + packet_class + packet_data_len + packet_ip_bytes
    return new_packet


def dns_udp_server(ip: int, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((ip, port))
    print("Server started successfully! waiting for data...")
    while True:
        try:
            data, addr = server_socket.recvfrom(DEFAULT_BUFFER_SIZE)
            dns_handler(data)
        except Exception as err:
            print(f"the error: {str(err)}")
