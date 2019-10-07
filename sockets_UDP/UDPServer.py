import socket

class UDP_Server:
	paqueteRecibido = ""
	paqueteAEnviar = ""

	def __init__(self, ip, puerto):
		self.ipServer = ip
		self.puertoServer = puerto

	def inicio(self):   
		# SOCK_DGRAM: Este protocolo nos da una conexión no fiable. (UDP)
		serverSocketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		serverSocketUDP.bind((self.ipServer, self.puertoServer))
		
		print ("El servidor esta esperando para recibir...")

		while True:

			mensaje, direccionIP = serverSocketUDP.recvfrom(1024)
			paqueteRecibido = mensaje
			print(f"cliente conectado desde la IP : {direccionIP} ")
			paqueteAEnviar = "conectado al servidor"
			serverSocketUDP.sendto(paqueteAEnviar.encode(), direccionIP)
		

		
class MainUDP_Server:
	s = UDP_Server("127.0.0.1", 5012)
	s.inicio()
	






