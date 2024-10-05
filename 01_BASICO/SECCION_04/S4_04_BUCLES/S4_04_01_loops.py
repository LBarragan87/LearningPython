#loop for

nombres = ["juan", "ana", "carlos","belen","fran"]

for nombre in nombres:
    print (f"Hola {nombre}")
    
lista = ["a","b","c"]

for letra in lista:
    numero_letra=lista.index(letra)+1
    print (f"Letra {numero_letra} es {letra}")    

palabra = "python es genial"
for letra in palabra:
    print(letra)
    
lista_numeros = [[1,2],[3,4],[5,6]]

for sublista in lista_numeros:
    print (sublista)
    
for dato1,dato2 in lista_numeros:
    print (dato1)
    print (dato2)
    
dic = {"clave1":"a","clave2":"b","clave2":"c"}
for item in dic.items():
    print(item)