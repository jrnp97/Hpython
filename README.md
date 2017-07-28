# Hacking con Python #

Guia en base a curso de hacking con python de @jdaniel conocido como Adastra en el mundo del hacking pueden encontrar el curso gratuito aqui --> `http://clkmein.com/qBVMFo` <--

A continuación les describire un poco de las diferentes librerias mencionadas en el curso

## Socket  -basico ##

Nos permite la creación de socket's para el envio de paquetes por medio de nuestra red, los cuales deben cumplir 2 condiciones una maquina destino y una maquina origen (la nuestra).


Para más información acerca del concepto puede consultar en https://www.ecured.cu/Socket.

* Es una libreria por defecto en python para utilizarla simplemente se importa `import socket`

En el script *banner_grabbing.py* se hace uso de esta brevemente para el reconocimiento de banners con vulnerables, se preguntaran que es un banners, bueno

Cuando uno realiza un scaneo de puertos normalmente se puede apreciar algo como 

![](images/1.png)

La descripción del servicio (tercera columna SERVICE), es el banner del software o servicio, por lo general mediante este se pueden identificar software con vulnerabilidades ya explotadas.


## Subprocess + ping ##


Se crea de un script para encontrar las maquinas activas en un segmento de red por medio de paquetes ICMP, utilizando el modulo mencionado.

ICMP es un protocolo simple entre el intercambio de maquinas el cual consiste enviar una peticion tipo ECHO_REQUEST a un HOST y espera un tiempo determinado la respuesta tipo ECHO_REPLY del host, pero no son los unicos mensajes que maneja este protocolo.

Por lo general se establece el funcionamiento del protocolo en la capa de enlace del modelo OSI, pero se puede apreciar su funcionamiento en comandos como PING 


Ya explicado lo mas basico del protocolo ICMP, haré referencia al modulo subprocess de python el cual permite ejecutan comando en el sistema, es decir ejecutar aplicaciónes o comandos que normalmente se ejecutan por terminal, comandos como (sistemas unix):

* ping (usado para este ejemplo)
* curl 
* nc

El script donde se usa el modulo subprocess para la utilización del comando ping lleva como nombre *basic_recon.py*


## DNSPython ##

Un DNS (Server Domain Name) es un servidor de nombres de dominio, el cual se encarga de procesar una dirección URL para la correcta conexión con el servidor web el cual cuenta con una dirección IP asociada a la URL.

A si mismo el proceso puede ser totalmente inverso, procesar IP's para la extracción de las URL's asociadas a estas.

Se hubican predeterminadamente en el puerto 53 manejando el protocolo UDP perteneciente a la capa 4 de transporte del modelo OSI, y para acciones como transferencias de zona, o backups utiliza el protocolo TCP en el mismo puerto 53.

Existen tipos de consultas especificas hacia los servidores de correo las que destacaremos por el momento serán

* **A** - Consultar dirección IPv4.
* **AAAA** - Consultar dirección IPv6.
* **MX** - Consultar servidor de correo.
* **NS** - Consulta de nombre de servidor.
* **TXT** - Consultar información textual.

Bueno ya explicado lo mas basico sobre un servidor DNS hablaremos de DNSPython es una libreria o modulo en python que permite realizar consultar contra registros DNS lo que indica que permite el acceso a alto nivel, pero tambien de bajo nivel al hacer manipulacion directa de zonas, mensajes, nombres o dominios.

Para mas información https://es.wikipedia.org/wiki/Sistema_de_nombres_de_dominio

Para la instlación de DNSPython se puede utilizar pip `$ pip install DNSPython`

En el siguiente script se realizan ejemplos de procesos con DNSPython

`dns_consult.py`




