import socket

class TCP_Server:

	def __init__(self, ip, puerto):
		self.ipServer = ip
		self.puertoServer = puerto

	def inicio(self):   
		#AF_INET: hace referencia a IPv4,
		#SOCK_STREAM: protocolo nos da una comunicación fiable de direcciones en un flujo de datos TCP
		serverSocketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#blind:  metodo para designacion de IP y Puerto para el socket 
		serverSocketTCP.bind((self.ipServer, self.puertoServer))
		# Esperando a un posible cliente
		print("***** Servidor TCP iniciado...  ****")
		print("esperando a clientes ...")
		# Para mantener el servidor tcp abierto
		while True:
			# Esperanda un posible cliente
			serverSocketTCP.listen(1)
			#coneccionSocket : objeto cliente
			# direccionIP: direccion IP
			# serverSocketTCP.accept(): El método accept() espera una conexión. Cuando llega, este acepta la conexión
			coneccionSocket, direccionIP = serverSocketTCP.accept()
			print(f"cliente conectado desde la IP : {direccionIP} ")
			mensaje_response = "conectado al servidor TCP..."
			# envía una respuesta (texto u otros datos) al cliente en el standar  estandar "utf-8" 
			coneccionSocket.send(mensaje_response.encode('utf-8'))
			coneccionSocket.close()
		
class MainTCP_Server:
	s = TCP_Server("127.0.0.1", 5030)
	s.inicio()




