class Humano:
	#Metodos
	def __init__(self, edad):
		#atributos
		self.edad = edad


	def hablar(self, mensaje):
		print mensaje

class IngSistema(Humano):
	def programar(self, lenguaje):
		print 'Voy a programar en', lenguaje

class LicDerechos(Humano):
	def estudiarCaso(self,de):
		print 'Voy a estudiar el caso de', de
		

#objeto o Instancia 
Pedro = IngSistema(30)
Raul = LicDerechos(45)

#acceder a un atributo 
#print 'Soy Raul y tengo', Pedro.edad
#print 'soy Raul y tengo', Raul.edad 
Pedro.programar('Python')
Raul.estudiarCaso('pedro')

Raul.hablar('hola')
Pedro.hablar('hola soy pedro')
				