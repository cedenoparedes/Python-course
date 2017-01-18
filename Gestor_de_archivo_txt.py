import glob, os 
from os import listdir, path
from sys import exit

os.chdir("C:\Users\ecedeno\Documents\project\python course")



def Directorios():
	for file in glob.glob("*.txt"):
		print file
	

def CreaNombre():
	nombres = str(raw_input('escriba el nombre del archivo: ')+'.txt')
	return nombres


def CrearArchivo(filename):
	archivo=open(filename,'w')
	archivo.close()
	print 'Archivo creado'
	return archivo

def EscribirArchivo(nombres):
	archivo=open(nombre,'a')
	archivo.write (raw_input('Escriba el texto a resibir: ')+'\n')
	archivo.close()

def ValidarArchivo(nombre):	
	return path.isfile(nombre)		

def LeerArchivo(archico):
	archivo=open(archico,'r')
	linea=archico.readline()
	while linea:
		print linea,
		linea=archivo.readline()
	archivo.close() 		

def Exit_program():
	exit()


while True:
	print 'seleccione su operacion'
	print '1.- Crear archivo'
	print '2.- Escribir en el archivo'
	print '3.- leer un archivo'
	print '4.- Salir'
	opcion = input('Escribe tu opcion: ')
	if opcion == 1:
		nombre = CreaNombre()
		if ValidarArchivo(nombre):
			print "el nombre exis"
		else:
			Archico = CrearArchivo(nombre)
			EscribirArchivo(Archico)
	elif opcion == 2:
		Directorios()
		nombre = CreaNombre()
		EscribirArchivo(nombre)
	elif opcion == 3:
		Directorios()
		nombre = CreaNombre()
		LeerArchivo(nombre)
	elif opcion == 4:
		Exit_program()
		