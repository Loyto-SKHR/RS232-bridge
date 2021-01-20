import socket
import time
import threading

hote = "localhost"
port = 12418

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((hote, port))

boucleC = True
def receptionServer():
	global server
	global boucleC
	while boucleC:
		msgRecu = server.recv(4096)
		msgRecu = msgRecu.decode()
		print(msgRecu)
		if(msgRecu == "stopdeconnexion"):
			boucleC = False
		else:
			pass
			#ser.write(msgRecu)

threadReceptionServer = threading.Thread(target=receptionServer, args=())
threadReceptionServer.start()

while boucleC:
	msgT = input(": ")
	msgT = msgT.encode()
	server.send(msgT)

	if(msgT == b"stopdeconnexion"):
		boucleC = False

server.close()
