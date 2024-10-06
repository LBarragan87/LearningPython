'''
Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.
'''

def reducir_lista(lista_numeros):
    listaDepurada=set(lista_numeros)
    nuevaLista=list(listaDepurada)
    nuevaLista.reverse()
    nuevaLista.pop(0)
    return nuevaLista

def promedio(lista_reducida):
    cantidadNumeros=len(lista_reducida)
    suma=0
    for numero  in lista_reducida:
        suma=suma+numero
    promedio = suma/cantidadNumeros
    return promedio
    
lista_numeros=[1,1,15,1,2,3,5,7,4,6,5]
print(reducir_lista(lista_numeros))
print(promedio(reducir_lista(lista_numeros)))
