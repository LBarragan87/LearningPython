'''
crear un analizador de texto:
-pedir a usuario un texto
-pedir a usuario 3 letras

devolver a usuario:
-cuantas veces aparece cada letra elejida
-cuantas palabras hay en el texto
-primera letra del texto y cual es la ultima
-palabras en orden inverso
-aparece palabra "python"?
'''

import os

os.system("cls")

texto = input("ingrese un texto: ")
texto_mayusculas = texto.upper()
cantidad_letras_usuario=3
confirmar_existencia_palabra=("python").upper()

lista_letras=[]
x=1
while x <= cantidad_letras_usuario:
    lista_letras.append((input(f"({x}) Ingrese letra a buscar: ")).upper())
    x+=1

print (f"ingresaste el texto: '{texto}'")
os.system("cls")
print ("---respuestas---")
print ("---respuesta 1---")
y=1
for letra in lista_letras:
    print(f"({y}) la letra {letra} aparece {texto_mayusculas.count(letra)} veces.")
    y+=1
   

texto_a_lista=texto.split()
texto_reversa=texto_a_lista.copy()
texto_reversa.reverse()
cantidad_palabras=len(texto_a_lista)
print ("---respuesta 2---")
print (f"El texto ingresado contiene {cantidad_palabras} palabras.")
print ("---respuesta 3---")
print (f"La primera letra del texto es {texto[0]}, y la ultima letra es {texto[-1]}")

mensaje_reversa=""
for palabra in texto_reversa:
    mensaje_reversa= f"{mensaje_reversa}{palabra} "

print ("---respuesta 4---")
print (mensaje_reversa)

print ("---respuesta 5---")
if confirmar_existencia_palabra in texto_mayusculas:
    print (f"la palabra '{confirmar_existencia_palabra}' SI aparece en el texto")
else:
    print (f"la palabra '{confirmar_existencia_palabra}' NO aparece en el texto")