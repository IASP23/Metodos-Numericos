import modRaices  
import math as mh 

a = float(input('Ingrese el coeficiente a'))
b = float(input('Ingrese el coeficiente b'))
c = float(input('Ingrese el coeficiente c'))

valores = modRaices.raices(a,b,c)
print (valores)

cantidad = modRaices.cant(a,b,c)
print (cantidad)