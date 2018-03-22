import sys
import socket 
import lib
from lib import Lib

PORT = 9000
BUFSIZE = 1000

def main(argv):
    clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #checks if input is correct
    if len(argv) == 2:
        serv = argv[0]
        msg = argv[1]
    else:
        print("Formatet skal vaere <server IP> <sti/Filnavn>")
        sys.exit()
    
    #client connects to server
    clisock.connect((serv, PORT))
    print("Connection til server etableret")
    
    #writes the filename t the server
    Lib.writeTextTCP(msg, clisock)

    #gets the filsize
    size = Lib.getFileSizeTCP(clisock)
    print("filstorelsen er: {}".format(size))
    dataread = 0

    #checks if the file exsists and if it does it starts receiving the file
    if size > 0:
        filename = Lib.extractFilename(msg)
        print("Filnavnet er: {}".format(msg))

        file = open(filename, 'wb')
        
        while dataread < size:
            filedata = clisock.recv(BUFSIZE)
            file.write(filedata)
            dataread = dataread+len(filedata)

        print("filen er faerdigoverfort")

    else:
        print("File not found on server")
        sys.exit()

    clisock.close()
       
    
    
def receiveFile(fileName,  conn):
	pass

if __name__ == "__main__":
   main(sys.argv[1:])
