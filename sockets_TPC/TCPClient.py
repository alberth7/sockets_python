import socket
import codecs
class TCP_Client:

    def __init__(self, nombreDelServer, puertoDelServer):
        self.ip = nombreDelServer
        self.puerto = puertoDelServer

    def iniciar(self):

        clienteSocketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clienteSocketTCP.connect((self.ip, self.puerto))
        mensaje_Response = clienteSocketTCP.recv(1024).decode('utf-8')
        print( mensaje_Response)
        
        mensaje_Request = input("mensaje a enviar: ")
        clienteSocketTCP.send(mensaje_Request.encode('utf-8'))
        
        mensaje_Response = clienteSocketTCP.recv(1024).decode('utf-8')
        print( mensaje_Response)
        clienteSocketTCP.close()

    
class MainTCP_Client:
    c = TCP_Client("127.0.0.1", 5055)
    c.iniciar()

