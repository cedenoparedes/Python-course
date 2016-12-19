


def main():
    
    
    def sumar(a,b):
        return a+b   
   
    def restar(a,b):
        return a-b

    def multiplicacion(a,b):
        return a*b  

    def division(a,b):
        return a/b

    print "Calculadora"
    print "Bienvenido"
    print "Introdusca el primer numero"
    a = int(raw_input())
    print "Introdusca el segundo numero"
    b = int (raw_input())
    print "Seleccione la Operacion Sum:1,rest:2,mult:3,div:4"
    seleccion = int (raw_input())

    if seleccion == 1:
        print (a,"+",b,'=',sumar(a,b))
    elif seleccion == 2:
        primerrint (a,"-", b, "=",restar(a,b))
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
     
    again()

def again():
    print "precione Y para vorver a inicio N para salir"
    calc_again = str(raw_input())

    if calc_again.upper() == 'Y':
        main()
    elif calc_again.upper() == 'N':
        print ('Bye.')
    else:
        again()


main()

