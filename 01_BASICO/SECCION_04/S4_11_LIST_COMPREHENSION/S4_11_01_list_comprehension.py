palabra = "python"

lista=[]
for letra in palabra:
    lista.append(letra)
    
print (lista)

# usando list comprehension
nueva_lista=[letra for letra in palabra if letra !="t"]
print (nueva_lista)

lista_rango = [n*10 for n in range(8,21)]
rango=range(7,15)
print(lista_rango)
print (rango)

pies = [10,20,30,40,50]
metros = [pie*12*0.0254 for pie in pies]
print (metros)