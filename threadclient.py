import socket
Client = socket.socket()
host = '127.0.0.1'
port = 2004
print('Waiting for connection response')
try:
    Client.connect((host, port))
except socket.error as e:
    print(str(e))
res = Client.recv(1024)
while True:
    Input = input('enter message: ')
    Client.send(str.encode(Input))
    res = Client.recv(1024)
    print(res.decode('utf-8'))
Client.close()
