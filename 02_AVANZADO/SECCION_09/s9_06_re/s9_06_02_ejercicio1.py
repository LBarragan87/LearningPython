'''
Crea una función llamada verificar_email para comprobar si una dirección de
email es correcta, que verifique si el email dado como argumento contiene
"@" (entre el nombre de usuario y el dominio) y finaliza en ".com"
(aunque aceptando también casos que cuentan con un dominio adicional, tal
como ".com.br" para el caso de un usuario de Brasil).

Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el
mensaje "Ok", pero si detecta que la frase no contiene los elementos indicados,
debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el
mensaje.
'''


import re

texto = "usuario@host.com.br"


def verificar_email(email):
    expresion = r"\w+\D?\w+[@].+[.]\w+[.]?\w"

    if re.match(expresion, email):
        print("Ok")
        return "Ok"
    else:
        print("La dirección de email es incorrecta")
        return "La dirección de email es incorrecta"


verificar_email(texto)
