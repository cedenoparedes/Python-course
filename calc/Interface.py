def operador1(paramA):
	for a in range(13):
		if paramA == 1:
			print paramA,"x",a,"=",Operaciones.multiplicacion(a,paramA)
		elif paramA <= 12:
			print paramA,"x",a,"=",Operaciones.multiplicacion(a,paramA)
		elif paramA == 0:
			print 'Valor valido'
		elif paramA >= 12:
			print 'Valor no valido'
		else:
			print 'Valor no valido'