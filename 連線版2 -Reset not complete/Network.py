import socket

class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP
        self.serverIP = "127.0.0.1"
        self.serverPort = 9487
        self.serverAddr = (self.serverIP,self.serverPort)
        self.id = self.connect()
        self.ready = False
        self.client.settimeout(0.1)

    def connect(self) -> int:
        self.client.connect(self.serverAddr)
        return int(self.client.recv(2048).decode())
    
    def send(self,x:int,y:int) -> None:
        data = str(x)+","+str(y)
        self.client.send(data.encode())