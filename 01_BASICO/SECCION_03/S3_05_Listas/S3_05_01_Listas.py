mi_lista=["a","b","c","z","w","x"]
mi_lista3=mi_lista.copy()
mi_lista2=["d","e","f"]
x=zip(mi_lista,mi_lista2)
resultado=len(mi_lista)
print (type(mi_lista))
print (resultado)
print (mi_lista[1:])
print (mi_lista.index("a"))
print (mi_lista+mi_lista2)
print (tuple(x))


mi_lista.sort()


mi_lista.pop(1)
print (mi_lista3)
print (mi_lista)


# filtrando
nueva_lista=[1,2,3,4,5,7,9,10,11,13,15,18]
pares_filter=filter(lambda dato_lista:(dato_lista%2 == 0),nueva_lista)
pares=list(filter(lambda dato_lista:(dato_lista%2 == 0),nueva_lista))
pares_copy=pares.copy()
print (pares)
print(pares_copy)
print(type(pares))


lista_desordenada=[3,8,1,6,5,10]
lista_ordenada=(lista_desordenada.copy())
lista_ordenada.sort()
lista_reversa=(lista_ordenada.copy())
lista_reversa.reverse()
print(lista_desordenada)
print(lista_ordenada)
print(lista_reversa)