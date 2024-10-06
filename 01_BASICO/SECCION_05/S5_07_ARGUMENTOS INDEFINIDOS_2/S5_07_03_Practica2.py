#Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.

def lista_atributos(**kwargs):
    keywords=[]
    for valor in kwargs.values():
        keywords.append(valor)
    return keywords

print (lista_atributos(x=1,y=2,z=3,w=4))