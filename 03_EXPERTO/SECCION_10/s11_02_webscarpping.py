import bs4
import requests


resultado = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")


sopa = bs4.BeautifulSoup(resultado.text, "lxml")

# print(sopa.select('title')[0].get_text())

parrafo_especial = sopa.select('p')[3].getText()

print(parrafo_especial)

columna_lateral = sopa.select(".section span")
print(columna_lateral[0])
