#Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.

def cantidad_atributos(**kwargs):
    conteo=0
    for llave,parametro in kwargs.items():
        conteo=conteo+1
    return conteo

print(cantidad_atributos(x=1,y=2,z=3,w=4))