import sys
import socket
import lib
from lib import Lib

HOST = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000

def main(argv):
    #creating an INET an streaming socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind to the HOST id and port 9000
    sock.bind((HOST, PORT))

    #The server can queue up to 5 connect requests
    sock.listen(5)

    print("Server socket opened")

    while True:
        #accepts connection from client
        clisock, addr = sock.accept()

        print("connection from {} achieved".format(addr))

        #reads the message from the client
        msg = readTextTCP(clisock)

        print("received following message: {} ".format(msg))

        #if the message is close it will close the connections and exit
        if msg == "close":
            sock.close()
            print("Server socket closed")
            clisock.close()
            sys.exit()

        #checks if the file exists and returns the size of the file, if it doesn't exist it returns 0
        size = check_File_Exists(msg)

        if size > 0:
            print("The size of the file is: {} bit".format(size))
            #converts the size of the file to a string and sends it to the client
            returnmsg = str(size)
            writeTextTCP(returnmsg, clisock)

            #opens the requested file
            file = open(msg, 'rb')

            #reads BUFSIZE bits from the file
            filedata = file.read(BUFSIZE)

            #while there is data to be read it will send the data and read new data
            while filedata:
                clisock.send(filedata)
                filedata = file.read(BUFSIZE)

        else:
            print("The file doesn't exist")
            #converts the size of the file to a string and sends it to the client
            returnmsg = str(size)
            writeTextTCP(returnmsg, clisock)


        clisock.close()





def sendFile(fileName,  fileSize,  conn):
    pass


if __name__ == "__main__":
   main(sys.argv[1:])
