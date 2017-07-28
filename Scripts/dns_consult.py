#!/usr/bin/python3.5

#Importando modulos a usar
import dns
import dns.resolver as DNS

## CONSULTAS A URL

#Realizando consulta de dirección IPv4 a URL google.com

ansA = DNS.query('google.com', 'A')

for a in ansA:
	print ("\n\n\tURL google.com Dirección IP {0}\n".format(a))

#Realizando consulta a servidores de correo a google.com

ansMK = DNS.query('google.com', 'MX')
print ("\n\n\tLista de servidores de correo\n")
for a in ansMK:
	print (" "+str(a))

#Realizando consulta para servidores de nombre

ansNS = DNS.query('google.com', 'NS')

print ("\n\n\tLista de servidores de nombre\n")
for a in ansNS:
	print (" "+str(a))

#Realizando consulta para direcciones IPv6

ansAAAA = DNS.query('google.com', 'AAAA')
for a in ansAAAA:
	print ("\n\n\tURL google.com Dirección IP {0}\n".format(a))

#Realizando consulta para registro de tipo SOA (Service Oriented Architecture)

ansSOA = DNS.query('google.com', 'SOA')
print ("\n\n\tLista de Servicios orientados a la arquitectura 'SOA'\n")
for a in ansSOA:
	print (" "+str(a))

#Realizando consultas textuales
ansTXT = DNS.query('google.com', 'TXT')
print ("\n\n\tLista de consulta textual\n")
for a in ansTXT:
	print (" "+str(a))

## CONSULTA A NOMBRES DE DOMINIO

import dns.name as DNS2

n = DNS2.from_text('www.google.com')
n1 = DNS2.from_text('google.com')

#Verificando si el dominio 2 es subdominio del dominio 1

print ("\n\n\t ¿ {0} es subdominio de {1} ? : {2}".format(n1, n, n1.is_subdomain(n)) )

#Proceso inverso

print ("\n\n\t ¿ {0} es subdominio de {1} ? : {2}".format(n, n1, n.is_subdomain(n1)) )


#Verificando diferencias entre dominios

print ("\n\n\tLas diferencias entre {0} y {1} son : {2}".format(n, n1, n.relativize(n1)))

#Imprimiendo partes del dominio

print ("\n\n\t El dominio {0} esta compuesto de la siguiente forma {1}".format(n1,n1.labels))

print ("\n\n\t El dominio {0} esta compuesto de la siguiente forma {1}".format(n,n.labels))

## CONSULTAS A DIRECCIONES IP

import dns.reversename as DNS3

n = DNS3.from_address('216.33.197.56')

print ("\n\n\tNombre de dominio de 216.33.197.56 : {0}".format(n))

print ("\n\n\tIP {0} del dominio {1}".format(DNS3.to_address(n), n))

## PETICIONES AXFR para transferencias de zona

import dns.query as DNS4
import dns.zone as DNS5

#Tratando de hacer una transferencia de zona de X IP a Y IP

trans = DNS5.from_xfr(DNS4.xfr('IP X', 'IP o dominio Y'))

