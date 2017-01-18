import glob, os

os.chdir("C:\Users\ecedeno\Documents\project\python course")



def main():	

	print 'para ecribir en el archivo presione T o un nuevo archivo para crear F'
	seleccion = str(raw_input())	
	if seleccion.upper() == 'T':
		print escribir()
	elif seleccion.upper() == 'F':
		print asignar_nombre(),creararchivo()
	else:
		main()

#def asignar_nombre():
	print 'Escriba el nombre del archivo'
	nombre_archivo = str(raw_input())
	

def Directorios():
	print 'Escriba el archivo que desea editar'
	for file in glob.glob("*.txt"):
		return file	
	

def creararchivo():
	archivo=open('nombre_archivo','w')
	archivo.close()
	main()

def escribir():
	archivo=open(str(raw_input()),'a')
	archivo.write((raw_input)('Escriba el texto a recibir: ')+'\n')
	archivo.close()
	main()

 

main()





		
