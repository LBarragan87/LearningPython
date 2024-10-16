'''
El código postal de una región determinada se forma a partir de dos caracteres
alfanuméricos y cuatro numéricos a continuación (ejemplo: XX1234). Crea una
función, llamada verificar_cp para comprobar si el código postal pasado como
argumento sigue este patrón. Si el patrón es correcto, mostrar al usuario el
mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".
'''
import re


def verificar_cp(cp):
    expresion = r"\w{2}\d{4}"
    if re.match(expresion, cp):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")


verificar_cp("asfgasdfasfdh")
verificar_cp("32asdf")
verificar_cp("as4863")
verificar_cp("as_4736")
verificar_cp("!af3573")
