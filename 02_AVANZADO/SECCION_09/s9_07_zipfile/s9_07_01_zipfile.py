import zipfile
'''
mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "w")
mi_zip.write("prueba4.txt")
mi_zip.close()
'''

zip_abierto = zipfile.ZipFile("archivo_comprimido.zip", "r")
zip_abierto.extractall()
