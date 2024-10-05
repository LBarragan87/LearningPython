#otra forma de concatenar texto
texto1="hola"
texto2="mundo"
texto_concat=texto1 + " " + texto2
print (texto_concat)

#multiplicar veces texto
texto_multi=(texto1*5)
print(texto_multi)

#texto multilineal
texto3="""asdf
zxcv
qwer"""

print (texto3)

#comprueba si un texto esta contenido dentro del texto principal
prueba_contiene="asdf" in texto3

print(prueba_contiene)

#longitud de un texto
largo_texto=len(texto1)
print (largo_texto)

nombre="LUIS"
nombre=nombre[0].upper()+nombre[1:].lower()
print (nombre)

nombre = "LUIS EDUARDO BARRAGAN HUERTA"
nombre_separado=nombre.split(" ")

parcial_nombre=""
for cada_nombre in nombre_separado:
    parcial_nombre=f"{parcial_nombre}{cada_nombre[0].upper()+cada_nombre[1:].lower()} "
    
    
print (parcial_nombre)