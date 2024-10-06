'''
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.
'''

def devolver_distintos(a,b,c):
    valores_lista=[a,b,c]
    valores_lista.sort()
    suma = a+b+c
    if suma>15:
        valor=f"el valor mas alto es {valores_lista[2]}"
    elif suma<10:
        valor=f"el valor mas bajo es {valores_lista[0]}"
    else:
        valor=f"el valor intermedio es {valores_lista[1]}"
    return (f"la suma de los valores es {suma}",valor)        
print (devolver_distintos (3,4,5))
print (devolver_distintos (3,1,2))
print (devolver_distintos (2,3,5))
print (devolver_distintos (6,7,3))
