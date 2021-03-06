#!/usr/bin/env python3
import time
import serial
import socket
import threading

#Configuration du port serie
ser = serial.Serial(
	port='/dev/pts/6',
	baudrate = 2400,
	parity=serial.PARITY_EVEN,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.SEVENBITS,
	timeout=None
)

ser.flushInput()

#Configuration du socket
hote = ''
port = 12418
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((hote, port))
server.listen(5)

client, infosConexion = server.accept()

#Fonction du thread pour la reception depuis le client
boucleC = True
def receptionClient():
	global client
	global boucleC
	while boucleC:
		msgRecu = client.recv(4096)
		msgRecu = msgRecu.decode()
		if(msgRecu == "stopdeconnexion"):
			boucleC = False

#Fonction du thread pour arreter le programme
boucleA = True
def arretProgramme():
	global boucleA
	repA = ""
	while(boucleA):
		repA = input("Pour quittez le progrmme entrez 'oui': ")
		repA = repA.upper()

		if(repA == "OUI"):
			boucleA = False
			global client
			client.send(b"stopdeconnexion")
			global boucleC
			boucleC = False

#On démarre les thread
threadReceptionClient = threading.Thread(target=receptionClient, args=())
threadReceptionClient.start()
threadArretProgramme = threading.Thread(target=arretProgramme, args=())
threadArretProgramme.start()

#Boucle recuperation des donnees sur le peripherique serie et envoie au client
while boucleC:
	if(ser.in_waiting > 0):
		#Lecture du port serie
		x=ser.readline()
		client.send(x)
		print(x.decode())

boucleA = False
time.sleep(1)
client.close()
time.sleep(2)
server.close()
