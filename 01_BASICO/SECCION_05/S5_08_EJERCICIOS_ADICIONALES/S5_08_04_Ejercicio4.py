'''
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.
'''

def contar_primos(val_max):
    rango=list(range(2,val_max+1))
    numeros_primos=[]
    for numero in rango:
        if es_primo(numero):
            numeros_primos.append(numero)
    return (numeros_primos)
        
def es_primo(numero):
  for i in range(2,numero):
    if (numero%i) == 0:
        return False
  return True

print(contar_primos(23))
