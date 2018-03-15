import sys
import socket

HOST_IP = "10.0.0.1"
PORT = 9000
BUFSIZE = 2048

def main(argv):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind((HOST_IP, PORT))

    sock.listen(5)

    print("Server socket opened")

    clisock, addr = sock.accept()


