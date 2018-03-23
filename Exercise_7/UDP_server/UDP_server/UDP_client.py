import sys
import socket

HOST_IP = "10.0.0.1"
PORT = 9000
BUFSIZE = 2048

def main(argv):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind((HOST_IP, PORT))
    print("Server socket opened")

    while True:

        message = input("If you wish to know the uptime, please write u or U. If you wich to know the average loadtime, please write l or L: ")

        if message == "close":
            print("closing socket")
            sock.close()
        else:
            print("sending %s\n" % message)
            sent = sock. sendto(message, HOST_IP)

            print("Waiting to recieve\n")
            data, server = sock.recvfrom(BUFSIZE)

            if message == 'U' or message == 'u':
                print("The uptime is: %s\n" % data)

            elif message == 'L' or message == 'l':
                print("The loadaverage is: %s\n" % data)


if __name__ == "__main__":
    main(sys.argv)
    


