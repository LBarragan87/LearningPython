'''
Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
'''

def suma_cuadrados(*numeros):
    suma=0
    for numero in numeros:
        suma=suma+(numero**2)
    return suma

print(suma_cuadrados(2,3,4))