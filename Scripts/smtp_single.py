#!/usr/bin/python3.5

import socket
import sys

#Capturando los 2 argumentos ingresados por el usuario
target = sys.argv[1]
command = sys.argv[2]

#Estableciendo manejo de excepciones
try:
	#Creando socket para establecer conexion de tipo TCP
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#Estableciendo conexion
	sock.connect([target,25])
	#Capturando banner
	banner = sock.recv(1024)
	print (banner)
	#Verificando respuesta del servidor
	if '220' in banner:
		#Abriendo archivo de texto y estableciendo un alias f
		with open('../files/user.txt', 'r') as f:
			#Utilizando información del archivo
			for user in f:
				#Enviando comando de consulta al servidor
				sock.send(command+' '+user)
				#Capturando resultado de la consulta
				result = sock.recv(1024)
				#Verificando si el resultado es satisfactorio
				if '252' in str(result) or '250' in str(result):
					print ("Usuario valido"+str(user))
		#Cerrando archivo
		f.close()
	#Cerrando socket
	sock.close()
#Estableciendo respuesta al momento que se presente un tiempo de espera alto
except socket.timeout:
	print ("Timeout para "+str(target))
#Estableciendo respuesta si ocurre un error durante la conexion
except socket.error:
	print ("Timeoit para "+str(target))
