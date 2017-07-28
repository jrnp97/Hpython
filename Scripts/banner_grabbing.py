#!/usr/bin/python3.5
import socket
import sys

"""
Construyendo socket indicando host de origen son el primer argumento socket.AF_INET, y con el segundo parametro se indica el tipo de Socket que
sera en este caso de tipo STREAM
"""

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Definiendo rango x de equipos a analizar <192.168.1.x>

for host in range(4, 5):
	#abriento archivo en modo lectura que contiene lista de puertos a analizar
	ports = open('../files/ports.txt', 'r')
	#Abriendo archivo en modo lectura que contiene los banners de software o servicios vulnerables
	vulnbanners = open('../files/vulbanners.txt', 'r')
	#Realizando loop que analiza los puertos
	for port in ports:
		HOST = str(sys.argv[1])+'.'+str(host)
		PORT = str(port)
		#Iniciando manejo de posible excepcion
		try:
			#Conectandose al HOST y a su puerto en cuestion por medio de socket
			socket.connect((HOST, int(port)))
			print ("\n\t\x1b[1;33mCONECTANDO a HOST {0} PORT {1} \n".format(HOST, PORT))
			#Estableciendo segundos (1) a esperar en dar un timeout (tiempo de espera)
			socket.settimeout(1)
			#Capturando el banner retornado por el HOST
			banner = socket.recv(1024)
			#Iteramos la información de los banners establecidos para encontrar incidencias
			for vbanners in vulnbanners:
				#Verificando incidencia, Convirtiendo banner de formato bytes a string
				banner2 = str(banner, 'utf-8')
				if banner2.strip() in vbanners.strip():
					print ("\x1b[1;32mHOST con vulnerabilidad {0}".format( banner ))
					print ("HOST {0} PORT {1}".format(HOST, PORT) )
		except OSError:
			print("\n\x1b[1;31mNo se pudo establecer conexion con {0} en el puerto {1}".format(HOST, PORT) )

