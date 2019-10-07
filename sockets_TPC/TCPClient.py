import socket

class TCP_Client:

    def __init__(self, nombreDelServer, puertoDelServer):
        self.ip = nombreDelServer
        self.puerto = puertoDelServer

    def iniciar(self):

        clienteSocketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clienteSocketTCP.connect((self.ip, self.puerto))
        mensaje_request = " soy un cliente"
        clienteSocketTCP.send(mensaje_request.encode())
        mensajeRecivido = clienteSocketTCP.recv(1024)
        print(mensajeRecivido.decode())
        clienteSocketTCP.close()

class MainTCP_Client:
    c = TCP_Client("127.0.0.1", 5030)
    c.iniciar()

