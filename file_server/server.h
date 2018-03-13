#ifndef SERVER_H
#define SERVER_H
#include <stdio.h>


class Server
{
public:
    Server();
    sendFile(string fileName, long fileSize, int outToClient);
};

#endif // SERVER_H
