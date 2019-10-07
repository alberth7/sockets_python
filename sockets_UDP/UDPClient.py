import socket

class UDP_Client:

    paqueteRecibido = ""
    paqueteAEnviar = ""

    def __init__(self, nombreDelServer, puertoDelServer):
        self.ip = nombreDelServer
        self.puerto = puertoDelServer

    def iniciar(self):
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientSocket.sendto(("soy el cliente").encode(), (self.ip, self.puerto ))
        mensajeRecivido, serverAddress = clientSocket.recvfrom(1024)
        print(mensajeRecivido.decode())
        clientSocket.close()

class MainUDP_Client:
    c = UDP_Client("127.0.0.1", 5012)
    c.iniciar()



