#Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

def suma_menores(lista_numeros):
    suma=0
    for numero in lista_numeros:
        if numero>0 and numero<1000:
            suma=suma+numero
    return suma

lista_numeros=[2,3,5,15,-20,2000]
print(suma_menores(lista_numeros))