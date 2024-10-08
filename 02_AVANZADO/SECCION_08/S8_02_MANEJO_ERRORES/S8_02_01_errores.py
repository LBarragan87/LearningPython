# try -> except -> else -> finaly
# tipos de errores se pueden buscar en documentacion -built-in-exceptions
'''
    def suma():
    
    n1=int(input(f"Ingrese numero 1:"))
    n2=int(input(f"Ingrese numero 2:"))
    print(n1+n2)
    print("gracias por sumar")

#suma()
'''

'''try: 
    suma()
except ValueError:
    print("dato ingresado no numerico")
except TypeError:
    print("estas intentando concatenar tipos distintos") 
else:
    print("Hiciste todo bien")
finally:
    print("esto fue todo")
'''

import os
os.system("cls")
def pide_numero(numero):
    while True:
        try:
            this_number=int(input(f"Ingrese Numero {numero}: "))
        except ValueError:
            print("dato ingresado no numerico")
        else:
            return this_number
            break
        
def suma():
    n1=pide_numero(1)
    n2=pide_numero(2)      

    print(n1+n2)
    print("gracias por sumar")   
             
suma()