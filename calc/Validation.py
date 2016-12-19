class validation(object):
		"""docstring for validation"""
	def __init__(self):
		pass				

	if seleccion == 1:
		print a,"+",b,'=',sumar(a,b)
	elif seleccion == 2:
		primerrint a,"-", b, "=",restar(a,b)
	elif seleccion == 3:
		print (a,"*",b, "=",multiplicacion(a,b))
	elif seleccion == 4:
		print (a,"/",b, "=",division(a,b))
	elif seleccion == 4 and b== 0:
		print "Operacion no valida, seleccione un numero mayor a 0"
		print "Introdusca el segundo numero"
		b = int (raw_input())
		print (a,"/",b, "=",division(a,b))
	else:
		print "Operacion no valida"