'''
Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
'''
#para el test se cambia el nombre del archivo solicitado en el ejercicio

escribirArchivo=open( "prueba3.txt","a")
escribirArchivo.write("Nuevo inicio de sesión\n")
escribirArchivo.close()

leerArchivo=open("prueba3.txt")
print(leerArchivo.read())