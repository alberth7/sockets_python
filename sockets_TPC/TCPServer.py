import socket


class TCP_Server:

    def __init__(self, ip, puerto):
        self.ipServer = ip
        self.puertoServer = puerto

    def inicio(self):
        # AF_INET: hace referencia a IPv4,
        # SOCK_STREAM: protocolo nos da una comunicación fiable de direcciones en un flujo de datos TCP
        serverSocketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # blind:  metodo para designacion de IP y Puerto para el socket
        serverSocketTCP.bind((self.ipServer, self.puertoServer))
        # Esperando a un posible cliente
        print("***** Servidor TCP iniciado...  ****")
        print("esperando a clientes ...")
        # Para mantener el servidor tcp abierto
        while True:
            serverSocketTCP.listen(1)
            coneccionSocket, direccionIP = serverSocketTCP.accept()
            
            mensaje_Response ="------- Bienvenido al servidor TCP--------"
            coneccionSocket.send(mensaje_Response.encode())
			
            print(f"cliente conectado desde la IP : {direccionIP} ")
            mensaje_Request_Cliente = coneccionSocket.recv(1024).decode()
            
            mensaje_Response ="Mensje: <<" + mensaje_Request_Cliente + ">>, fue recepcionado correctamente."
            coneccionSocket.send(mensaje_Response.encode())

            coneccionSocket.close()

class MainTCP_Server:
    s = TCP_Server("127.0.0.1", 5055)
    s.inicio()




