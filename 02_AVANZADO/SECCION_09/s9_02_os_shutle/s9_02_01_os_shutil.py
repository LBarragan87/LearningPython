import os
import shutil


print(os.getcwd())

archivo = open("curso.txt", "w")
archivo.write("texto de prueba\n")
archivo.close()


print(os.listdir())
shutil.move("curso.txt", "E:\\04-CURSOS_UDEMY\\PYTHON\\02_AVANZADO\\SECCION_09"
            "\\s9_02_os_shutle")
