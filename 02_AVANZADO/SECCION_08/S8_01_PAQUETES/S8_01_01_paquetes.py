
print("---usando importaciones y llamadas desde paquete raiz---")
import MI_PAQUETE
import MI_PAQUETE.MI_SUB_PAQUETE
import MI_PAQUETE.MI_SUB_PAQUETE.saludo
import MI_PAQUETE.suma_resta

MI_PAQUETE.suma_resta.suma(50,30)
MI_PAQUETE.suma_resta.resta(50,30)
MI_PAQUETE.MI_SUB_PAQUETE.saludo.hola()


print("---usando importaciones, mas especificas y llamadas desde modulo raiz---")
from MI_PAQUETE import suma_resta
from MI_PAQUETE.MI_SUB_PAQUETE import saludo

suma_resta.suma(3,5)
suma_resta.resta(3,5)
saludo.hola()

print("---usando importaciones, mas especificas y llamadas para uso directo de funciones---")
from MI_PAQUETE.suma_resta import suma,resta
from MI_PAQUETE.MI_SUB_PAQUETE.saludo import hola

suma(3,5)
resta(3,5)
hola()


