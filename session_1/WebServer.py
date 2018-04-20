# import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
serverPort = 2879
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server address: {}'.format(gethostbyname(gethostname())))

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, address = serverSocket.accept()
    print('Connected Client: {}'.format(address))
    try:
        message = connectionSocket.recv(2048).decode()
        filename = message.split()[1]
        print(filename[1:])
        f = open(filename[1:], mode='rb')
        outputdata = f.read()
        print(outputdata)
        #Send one HTTP header line into socket
        status = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(status.encode())
        #Send the content of the requested file to the client
        connectionSocket.send(outputdata)
        """
        for i in range(0, len(outputdata)):
            print('Sending...')
            connectionSocket.send(outputdata[i].encode())
        print('Done!')
        """
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        status = "HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(status.encode())

        #Close client socket
        connectionSocket.close()

