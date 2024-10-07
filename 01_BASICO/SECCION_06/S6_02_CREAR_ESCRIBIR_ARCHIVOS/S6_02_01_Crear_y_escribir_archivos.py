#modos de apertura r->read(solo lectura, por defecto) / w -> write (escritura, si el archivo existe, se resetea, y si no existe, se crea) / a -> si agrega informacion al final del archivo, si no existe, el archivo se crea
    
archivo = open("prueba2.txt","w")
is_writable = archivo.writable()
if is_writable:
    archivo.write("soy el nuevo texto\\valor1\\valor2\n")   

archivo = open("prueba2.txt","a")
is_writable = archivo.writable()
if is_writable:
    archivo.write("soy el nuevo texto\\valor1\\valor2\n")
        
archivo.close()
archivo = open("prueba2.txt","r")
lineas=archivo.readlines()
for linea in lineas:
    print (linea.rstrip())
archivo.close()


#simulando lectura de datos desde archivo para ejercicios autocad
'''
archivo = open("prueba2.txt","r")
lineas=archivo.readlines()
for linea in lineas:
    separando_datos = linea.split("\\")
    solo_primer_dato= separando_datos
    print (solo_primer_dato)
archivo.close()
'''