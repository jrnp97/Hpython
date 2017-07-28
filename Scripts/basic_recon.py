#!/usr/bin/python3.5

from subprocess import Popen, PIPE

for ip in range (1,30):
	#Definiendo direccion ip
	IP = "192.168.1."+str(ip)
	"""
	Construyendo y ejecutando comando para utilizar ping equivalente a $ ping -c 1 IP, ademas de establecer los formatos de entrada, salida
	y error de los datos retornados por la ejecucion del comando
	"""
	subprocess = Popen(['/bin/ping', '-c 1', IP,], stdout=PIPE, stdin=PIPE, stderr=PIPE)
	#Capturando datos de ejecución
	stdout, stderr = subprocess.communicate(input=None)
	#Verificando la existencia del host
	
	if b"bytes from " in stdout:
		print ("Host encontrado {0} ".format(IP)) 
