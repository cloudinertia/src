#import socket module
from socket import *                                  
import time
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
#Fill in end
serverSocket.bind(('',6789))
serverSocket.listen(6789)
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept() #Fill in start              #Fill in end          
    message = connectionSocket.recv(1024)  #Fill in start          #Fill in end               
    filename = message.decode('utf-8').split()[1]
    try:
        print('filename',filename[1:])
        f = open(filename[1:])                        
        with open(filename[1:]) as f:
            outputdata = f.readlines()#Fill in start       #Fill in end                   
            print(outputdata)
            flatten = ""
            for item in outputdata:
                flatten += item 
            #Send one HTTP header line into socket
            connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')
            connectionSocket.send(str.encode('Content-Length: {}\r\n\r\n'.format(len(flatten))))
            connectionSocket.send(b'Content-Type: text/html; charset=utf-8\r\n\r\n')
            connectionSocket.send(b'date: Fri, 20 Apr 2018 15:47:01 GMT\r\n\r\n')
            #Fill in start
            #Fill in end                
            #Send the content of the requested file to the client
            for item in outputdata:           
                connectionSocket.send(str.encode(item))
            connectionSocket.close()
    except IOError as e:
        connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
        connectionSocket.send(b"Content-Type: text/html; charset=UTF-8\r\n\r\n")
        connectionSocket.send(b'File not found')
        connectionSocket.close()
