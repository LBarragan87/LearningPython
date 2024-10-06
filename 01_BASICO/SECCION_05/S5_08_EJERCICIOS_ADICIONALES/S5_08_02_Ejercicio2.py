'''
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d'
,
'e'
,
'i'
,
'n'
,
'o'
,
'r'
,
't']
'''

def letras_unicas_sorted(texto):
    nueva_lista_texto=[]
    for letra in texto:
        nueva_lista_texto.append(letra)
    texto_set=list(set(nueva_lista_texto))
    texto_set.sort()
    return print (texto_set)    

letras_unicas_sorted("entretenido")