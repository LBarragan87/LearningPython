nombres = ["ana","hugo","valeria"]
edades = [65,29,42]
ciudades=["lima","madrid","mexico"]

combinados = list(zip(nombres,edades,ciudades))
print ((combinados))

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años, y vive en la ciudad de {ciudad}")
    
