import numpy as np


print ('\tUniversidad de las Fuerzas Armadas ESPE-L\n')
print ('Metodos de integracion numerica')
print ('Metodo del Boole')

def funcion(x): #aquí va la funcion a evaluar

    res =  (x**2)*np.e**(-x**2)
    return res

# aqui se deben ingresar los valores de la integral
limite_inferior=1 #b
limite_superior=2#a
n=5 #tomamos el valor de n como 3 para este metodo

# se calcula h para la formula
h= (limite_superior-limite_inferior)/n  # (a-b) /n  recordando que n=3
# se calculan x0,x1,x2,x3.. 

x0= limite_inferior #x0=b
x1=x0+h #b+h
x2=x1+h 
x3=x2+h 
x4=x3+h
# calculamos las fx usando la funcion
fx0= funcion(x0)
fx1=funcion(x1)
fx2=funcion(x2)
fx3=funcion(x3)
fx4=funcion(x4)

resultado= (2/45)*(h)*(7*(fx0)+32*(fx1)+12*(fx2)+32*(fx3)+7*(fx4))
print ('Resultado', resultado)
print ('h',h)
