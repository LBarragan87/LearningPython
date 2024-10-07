#abrir y leer archivo
print("----leyendo archivo----")
mi_archivo=open('prueba.txt')
print(mi_archivo.read())
mi_archivo.close()

#abrir y leer linea por linea
#rstrip -> devuelve una version recortada a la derecha de la cadena
print("----leyendo lineas----")
mi_archivo=open('prueba.txt')
print(mi_archivo.readline().rstrip().upper())
print(mi_archivo.readline().rstrip())
print(mi_archivo.readline().rstrip())
mi_archivo.close()

print("----leyendo archivo e iterando lineas----")
mi_archivo=open('prueba.txt')
for line in mi_archivo:
    print(f"aqui dice {line.rstrip().upper()}")
mi_archivo.close()

print("----abriendo archivo y usando readlines----")
# lee las lineas como una lista
mi_archivo=open("prueba.txt")
todas = mi_archivo.readlines()
print (todas.pop())

mi_archivo.close()