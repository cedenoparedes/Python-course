def validate_number(data):
    if data.isdigit():
        data = int(data)
    else:
        data = None
    return data


    if edad >= 0 and edad < 18:
        print 'Eres un nino'
    elif edad >= 18 and edad < 30:
        print 'Eres un adolescente'
    elif edad >= 30 and edad < 60:
        print 'Eres adulto'
    elif  edad == None:
        print 'Debes instroducir un valor'
    else:
def main():

    print 'Instrodusaca su edad'
    edad = raw_input()
    edad = validate_number(edad)
    
        print 'Eres de la tercera edad'
    again()

def again():
    print 'Presione "Y" para evaluar su rango de edad o "N" para salir'
    edad_again = str(raw_input())

    if edad_again.upper() == 'Y':
        main()
    elif edad_again.upper() == 'N':
        print ('bye.')
    else:
        again()

main()
    
    
