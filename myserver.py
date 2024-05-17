import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        host,port=self.client_address
        print("{}:{} wrote:".format(host,port))
        print(self.data.decode())
        msg=input("enter text .. ")
        self.request.sendall(msg.encode())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
