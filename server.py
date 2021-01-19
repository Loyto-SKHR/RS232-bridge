#!/usr/bin/env python3

#import des lib time, serial, socket, threading
import time
import serial
import socket
import threading

#Configuration du port serie
#ser = serial.Serial(
#	port='/dev/ttyUSB0',
#	baudrate = 2400,
#	parity=serial.PARITY_EVEN,
#	stopbits=serial.STOPBITS_ONE,
#	bytesize=serial.SEVENBITS,
#	timeout=None
#)

#Configuration du socket
hote = ''
port = 12418
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((hote, port))
server.listen(5)

client, infosConexion = server.accept()

#Fonction du thread pour la reception depuis le client
def receptionClient():
	while 1:
		msgRecu = client.recv(4096)
		msgRecu = msgRecu.decode()
		print(msgRecu)
		#ser.write(msgRecu)

#On démarre le thread
threadR = receptionClient()

#Boucle recuperation des donnees sur le peripherique serie et envoie au client
#while 1:
	#if(ser.in_waiting > 0):
		#Lecture du port serie
		#x=ser.readline()
		#x = x.encode()
		#client.send(x)
