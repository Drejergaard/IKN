//============================================================================
// Name        : file_server.cpp
// Author      : Lars Mortensen
// Version     : 1.0
// Description : file_server in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <iknlib.h>
#include <netdb.h>
#include <

#define HOST  "10.0.0.1"
#define PORT  9000
#define BUFSIZE  1000

using namespace std;

void sendFile(string fileName, long fileSize, int outToClient);

/**
 * main starter serveren og venter på en forbindelse fra en klient
 * Læser filnavn som kommer fra klienten.
 * Undersøger om filens findes på serveren.
 * Sender filstørrelsen tilbage til klienten (0 = Filens findes ikke)
 * Hvis filen findes sendes den nu til klienten
 *
 * HUSK at lukke forbindelsen til klienten og filen nÃ¥r denne er sendt til klienten
 *
 * @throws IOException
 *
 */
int main(int argc, char *argv[])
{
    //variables
    int sockfd, newsockfd;
    socklen_t clilen;
    char buff[BUFSIZE];
    struct sockaddr_in serv_addr, cli_addr;
    int n, size;
    string msg, returnmsg;



    if (argc < 2)
    {
        printf("ERROR, no port provided\n");
        exit(1);
    }

    sockfd = socket(AF_INET, SOCK_STREAM, 0);

    if (sockfd < 0)
        error("ERROR opening socket");

    bzero((char *) &serv_addr, sizeof(serv_addr));

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr =htonl(16772161);
    serv_addr.sin_port = htons(PORT);

    if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)
        error("ERROR on binding");

    listen(sockfd, 5);

    while(true)
    {
        clilen = sizeof(cli_addr);
        newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);

        if (newsockfd < 0)
            error("ERROR on accept");
        else
            printf("Accepted connection from %s", cli_addr);



        bzero(buff, BUFSIZE);
        n = *readTextTCP(buff, BUFSIZE-1,newsockfd);

       if(n < 0)
           error("ERROR reading from socket");
       else
           printf("Message received: %s", buff);

       msg = (string)buff;

       if (msg == "close")
       {
           close(sockfd);
           close(newsockfd);
           return 0;
       }

       size = check_File_Exists(msg);

       if (size > 0)
       {
           returnmsg = (string)size;
           writeTextTCP(newsockfd, returnmsg);
       }

       file = open(msg)

    }

}

/**
 * Sender filen som har navnet fileName til klienten
 *
 * @param fileName Filnavn som skal sendes til klienten
 * @param fileSize Størrelsen på filen, 0 hvis den ikke findes
 * @param outToClient Stream som der skrives til socket
     */
void sendFile(string fileName, long fileSize, int outToClient)
{
    // TO DO Your own code
}

