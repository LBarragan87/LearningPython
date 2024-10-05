lista = [58,56,72,65,15]

print (f"el menor es {min(lista)} y el mayor es {max(lista)}")

nombres = ["juan","pablo","alicia","carlos"]
print (min(nombres))

nombre = "aA?1"
print (min(nombre)) #<--- el orden empieza por letras mayusculas y luego minusculas

texto_lista=[]
for letra in nombre:
    texto_lista.append(letra)

texto_lista.sort()
print (texto_lista)