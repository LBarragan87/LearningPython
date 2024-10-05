texto = "Hola Mundo Mundo Mundo"
# upper()
texto_upper=texto.upper()
print(texto_upper)

# lower()
texto_lower=texto.lower()
print(texto_lower)

# split()
texto_split=texto.split(" ")
print(texto_split)

# find(), diferencia con index -> en caso de no encontrar los caracteres, da index -1, en lugar de error
texto_find=texto.find("Mu")
print(texto_find)

#replace
texto_replace=texto.replace(" ",",")
print(texto_replace)

#join
a="hola"
b="mundo"
c=" "
d=c.join([a,b])
print (d)