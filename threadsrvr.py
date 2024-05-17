import socket
import os
from _thread import *
Server = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
try:
    Server.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
Server.listen(5)
def threaded_client(connection, t):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        response = "Thread "+str(t)+' says: ' + data.decode('utf-8')
        if not data:
            break
        print (response)
        connection.sendall(str.encode(response.upper()))
    connection.close()
while True:
    Client, address = Server.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    start_new_thread(threaded_client, (Client, ThreadCount))
    
ServerSideSocket.close()
