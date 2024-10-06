'''
Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"
'''

def numeros_persona(nombre,*numeros):
    suma_numeros=0
    for numero in numeros:
        suma_numeros=suma_numeros+numero
    return (f"{nombre}, la suma de tus números es {suma_numeros}")

print(numeros_persona("Luis",3,5,7,9,10,15))