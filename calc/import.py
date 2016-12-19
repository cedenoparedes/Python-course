import Operaciones
import Interface
import Operaciones

def main():

	print 'Hola Ezequiel'
	print 'Digite un numero'
	primernum = int(raw_input())

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
			else:
				main()

	operador1(primernum)
	main()

	
main()


