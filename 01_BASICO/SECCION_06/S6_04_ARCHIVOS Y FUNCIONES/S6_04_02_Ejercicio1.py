#Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).
def abrir_leer(archivo):
    thisFile= open(archivo)
    return thisFile.read()