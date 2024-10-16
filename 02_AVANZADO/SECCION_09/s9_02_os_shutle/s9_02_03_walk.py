import os
ruta = os.getcwd()
os.system("cls")
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"en la carpeta {carpeta}")
    print("las subcarpetas son:")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("los archivos son: ")
    for arch in archivo:
        print(f"\t{arch}")
