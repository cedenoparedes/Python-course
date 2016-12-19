def main():
	print 'soy el inicio'
	def again():
	    print "precione Y para vorver a inicio N para salir"
	    calc_again = str(raw_input())

	    if calc_again.upper() == 'Y':
	        main()
	    elif calc_again.upper() == 'N':
	        print ('Bye.')
	    else:
	    	again()

	again()	    	

main()


