'''
calculo de comiciones de vendedores 13%
-interfaz debe preguntar:
    * Nombre
    * Ventas

- Programa debe responder con mensaje que indique:
    * Nombre
    * Monto correspondiente a las ventas

'''

nombre = input("Indica tu nombre: ")
ventas = input("Indique monto de Ventas alcanzadas en el mes: ")
comision = float(ventas) * 0.13

print (f"Hola {nombre}, este mes ganaste $ {comision:,.2f}")