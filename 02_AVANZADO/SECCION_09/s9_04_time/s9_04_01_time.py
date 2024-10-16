import time
import timeit


def lista_range(numero):
    return list(range(1, numero))


def prueba_for(numero):
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


print("prueba for")
inicio = time.time()
(prueba_for(1000000))
final = time.time()
print(final-inicio)


print("prueba while")
inicio = time.time()
(prueba_while(1000000))
final = time.time()
print(final-inicio)


print("prueba lista range")
inicio = time.time()
(lista_range(1000000))
final = time.time()
print(final-inicio)


declaracion = '''
prueba_for(1000000)
'''

declaracion2 = '''
prueba_while(1000000)
'''

declaracion3 = '''
lista_range(1000000)
'''
setup1 = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return lista
'''

setup2 = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

'''

setup3 = '''
def lista_range(numero):
    return list(range(1, numero))
'''

duracion = timeit.timeit(declaracion, setup1, number=1)
duracion2 = timeit.timeit(declaracion2, setup2, number=1)
duracion3 = timeit.timeit(declaracion3, setup3, number=1)
print(duracion)
print(duracion2)
print(duracion3)