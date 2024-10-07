'''
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
'''
#para el test se cambia el nombre del archivo solicitado en el ejercicio

escribirArchivo=open("prueba3.txt","w")
escribirArchivo.write("Nuevo texto")
escribirArchivo.close()

leerArchivo=open("prueba3.txt")
print(leerArchivo.read())