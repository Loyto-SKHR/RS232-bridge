import socket
import time
import threading
import pyserial

#ser = serial.Serial(
#	port='COM9',
#	baudrate = 2400,
#       parity=serial.PARITY_EVEN,
#       stopbits=serial.STOPBITS_ONE,
#       bytesize=serial.SEVENBITS,
#       timeout=None
#)

numeroDePost = input("Entrez votre numéro de poste (ex: 154): ")
ipServLinux = "192.168.10." + numeroDePost
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
		if(msgRecu == "stopdeconnexion"):
			boucleC = False
		else:
			pass
			#ser.write(msgRecu)

boucleA = True
def arretProgramme():
        global boucleA
        repA = ""
        while(boucleA):
                repA = input("Pour quittez le progrmme entrez 'oui': ")
                repA = repA.upper()

                if(repA == "OUI"):
                        boucleA = False
                        global server
                        server.send(b"stopdeconnexion")
                        global boucleC
                        boucleC = False

threadReceptionServer = threading.Thread(target=receptionServer, args=())
threadReceptionServer.start()
threadArretProgramme = threading.Thread(target=arretProgramme, args=())
threadArretProgramme.start()

while boucleC:
	pass
	#if(ser.in_waiting > 0):
                #Lecture du port serie
                #x=ser.readline()
                #x = x.encode()
                #client.send(x)


server.close()
