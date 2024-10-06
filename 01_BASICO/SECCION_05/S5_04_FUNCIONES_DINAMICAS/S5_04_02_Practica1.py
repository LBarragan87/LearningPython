'''
Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.

No invoques la función, solo es necesario definirla.
'''

def todos_positivos(lista_numeros ):
    for numero in lista_numeros :
        Signo=numero>0
        if not(Signo):
            return False
            break
    return True




lista_numeros =[5,10,5]
print(todos_positivos(lista_numeros))

lista_numeros = [5,-10,5]
print(todos_positivos(lista_numeros))