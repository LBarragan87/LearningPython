#Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.

def cantidad_pares(lista_numeros):
    conteo=0
    for numero in lista_numeros:
        if numero%2 == 0:
            conteo=conteo+1
    return conteo

lista_numeros=[1,2,3,10,15,20,22,24,27]

print(cantidad_pares(lista_numeros))