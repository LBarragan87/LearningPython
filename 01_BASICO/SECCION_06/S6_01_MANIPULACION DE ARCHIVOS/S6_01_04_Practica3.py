'''
Abre el archivo texto.txt e imprime únicamente la segunda línea.
'''
mi_archivo=open("archivo_ejercicios_seccion1_ejercicio1.txt")
mi_archivo.readline()
print(mi_archivo.readline().rstrip())