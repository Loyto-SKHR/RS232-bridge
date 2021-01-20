#!/usr/bin/env python3
import socket
import time
import threading
import serial

ser = serial.Serial(
	port='/dev/pts/12',
	baudrate = 2400,
        parity=serial.PARITY_EVEN,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.SEVENBITS,
        timeout=None
)

numeroDePost = input("Entrez votre numéro de poste (ex: 154): ")
ipServLinux = "192.168.10." + numeroDePost
hote = "localhost"
port = 12418

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((hote, port))

boucleC = True
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

threadArretProgramme = threading.Thread(target=arretProgramme, args=())
threadArretProgramme.start()

while boucleC:
	msgRecu = server.recv(4096)
	msgRecu = msgRecu.decode()

	if(msgRecu == "stopdeconnexion"):
        	boucleC = False
	else:
		ser.write(msgRecu.encode())
		print(msgRecu)


boucleA = False
server.close()
