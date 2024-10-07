'''
Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

Imprime el contenido completo de "registro.txt" al finalizar.

Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.
'''
#para el test se cambia el nombre del archivo solicitado en el ejercicio
escribirArchivo=open( "prueba4.txt","a")
escribirArchivo.writelines(["Federico\t", "20/12/2021\t", "08:17:32 hs\t", "Sin errores de carga\n"])
escribirArchivo.close()

leerArchivo=open("prueba4.txt")
print(leerArchivo.read())