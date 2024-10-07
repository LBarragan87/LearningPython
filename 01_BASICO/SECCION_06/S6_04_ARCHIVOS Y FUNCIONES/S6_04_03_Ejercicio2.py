#Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

def sobrescribir(archivo):
    thisFile = open(archivo,"w")
    thisFile.write("contenido eliminado")
    