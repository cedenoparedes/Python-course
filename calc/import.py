import Operaciones

def validate_number(paramA):
    if paramA.isdigit():
        paramA = int(paramA)
    else:
        paramA = None
    return paramA

def main():

	print 'Hola Ezequiel'
	
	try:
		primernum = int(raw_input('Digite un numero'))
	except:
		print 'deves de introducir un numero'
		

	def operador1(paramA):
		for a in range(13):	
			if paramA == 1:
				print paramA,"x",a,"=",Operaciones.multiplicacion(a,paramA)
			elif paramA <= 12:
				print paramA,"x",a,"=",Operaciones.multiplicacion(a,paramA) 
			elif paramA == 0:
				print 'Numero no valido'
			elif paramA >= 12:
				print 'Numero no valido'
			elif paramA == None:
				print	'debes de digitar un numero'
			else:
				main()

	operador1(primernum)
   

	
main()


