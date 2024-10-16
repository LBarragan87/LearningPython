'''
Crea una función llamada verificar_saludo para verificar si una frase
entregada como argumento inicia con la palabra "Hola". Si se encuentra
el patrón, la función debe finalizar mostrando el mensaje "Ok", pero
si detecta que la frase no contiene "Hola", debe informarle al usuario
"No has saludado" imprimiendo el mensaje en pantalla.
'''

import re


def verificar_saludo(frase):
    expresion = r"^[Hola]"

    if re.match(expresion, frase):
        print("Ok")
    else:
        print("No has saludado")


frase = "chtm Hola a todos"
verificar_saludo(frase)
