'''
expresiones regulares:
\\d digito numerico
\\w caracter alfanumerico
\\s espacio en blanco
\\D no es digito numrico
\\W No alfanumerico
\\S no espacio en blanco


cuantificadores:
{n} se repite n veces
+ 1 o mas veces
{n,m} se repite de n a m veces
{n,} de n hacia arriba
* 0 o mas veces
? 1 o 0 veces
. comodin
^ al comienzo
& digito al final
[] excluir
'''

import re

texto = ("si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio"
         "de ayuda online")


'''
palabra = "ayuda" in texto
print(palabra)

patron = "ayuda"
busqueda = re.findall(patron, texto)
print(len(busqueda))

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())
'''

patron2 = r'\W(\d{3})\W-(\d{3})-(\d{4})'
resultado = re.search(patron2, texto)
print(resultado.group())
print(resultado.group(1))
print(resultado.group(2))
print(resultado.group(3))


clave = input("clave: ")
patron = r"\D{1}\w{7}"
chequear = re.search(patron, clave)
print(chequear)


texto = "no atendemos los lunes por la tarde"
buscar = re.search(r"lunes|martes", texto)
print(buscar)


texto = "hola              mundo             como          estan"
buscar = re.findall(r'[^\s]+', texto)
print(buscar)
