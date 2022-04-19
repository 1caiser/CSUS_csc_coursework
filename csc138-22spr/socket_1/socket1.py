'''Make sure to run the .py file standalone, running it
   within the IDE does not cause the program to work as 
   intended.
   '''

# Import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
HOST = ''
PORT = 80 # pick a port number
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

while True:
    # establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024) # receive 1024 bytes
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read(1024)
        # Send one HTTP header line into socket
        string200 = 'HTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.send(str.encode(string200))
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        string404 = 'HTTP/1.1 404 File Not Found\r\n\r\nThere is no world.'
        connectionSocket.send(str.encode(string404))
        # Close client socket
        connectionSocket.close()
serverSocket.close()