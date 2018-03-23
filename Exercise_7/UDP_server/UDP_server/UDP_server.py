import sys
import socket


HOST_IP = '10.0.0.1'
PORT = 9000
BUFSIZE = 2048
UP = "/proc/uptime"
LOAD = "/proc/loadavg"

def main(argv):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind((HOST_IP, PORT))

    print ("Server socket opened.\n")

    while True:
        print ("waiting to receive a message.\n")
        data, address = sock.recvfrom(BUFSIZE)

        print ("received %s bytes from %s" % (len(data), address))

        print (data)

        if data == 'U' or data == 'u':
            file = open(UP)
            filedata = file.read(BUFSIZE)

            sent = sock.sendto(filedata, address)
            print ("sent %s bytes back to %s" % (sent, address))

        elif data == 'L' or data == 'l':
            file = open(LOAD)
            filedata = file.read(BUFSIZE)

            sent = sock.sendto(data, address)
            print ("sent %s bytes back to %s" % (sent, address))


if __name__ == "__main__":
    main(sys.argv)