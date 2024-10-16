from collections import Counter
from collections import defaultdict
from collections import namedtuple

numeros = [8, 6, 9, 5, 4, 4, 4, 5, 5, 5, 8, 7, 4, 5, 4, 4]

serie = (Counter(numeros))
print(serie)
print(serie.most_common())
print(serie.most_common(1))
print(list(serie))


mi_dic = defaultdict(lambda: "nada")

print(mi_dic["uno"])


mi_tupla = (500, 18, 68)
print(mi_tupla[1])

persona = namedtuple("persona", ["nombre", "altura", "peso"])
ariel = persona("Ariel", 1.76, 79)
jorge = persona("carranza", 1.85, 85)
print(ariel.nombre)
print(ariel.altura)
print(ariel.peso)
print(jorge.nombre)
print(jorge.altura)
print(jorge.peso)
print(type(namedtuple))

x = namedtuple("w", ["nombre", "altura", "peso"])
z = x("luis", 1.80, 95)
print(z.nombre)
