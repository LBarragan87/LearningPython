mi_dic={"c1":"valor 1","c2":"valor2","c3":"valor 3"}
print (mi_dic)
print (mi_dic["c3"])

cliente = {"nombre":"luis","apellido":"barragan","edad":37,"peso":105,"altura":1.83}
cliente["color_ojos"]="verde"
cliente[5]="programador"
print (f"la altura de {cliente["nombre"]} es {cliente["altura"]}")
print (cliente)
print (cliente.values())
print (cliente.keys())
z=zip(cliente.keys(),cliente.values())
print (tuple(z))