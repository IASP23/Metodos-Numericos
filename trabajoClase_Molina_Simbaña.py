import numpy as np
from sympy import *
from numpy import log as ln
import math

# Metodo de simspon 3/8

def funcion(x): #aquí va la funcion a evaluar

    res = log(x-tan(np.e**(2*x)))
    return res

# aqui se deben ingresar los valores de la integral
limite_inferior=2 #b
limite_superior=2.5 #a
n=3 #tomamos el valor de n como 3 para este metodo

# La formula es (3/8)(h)((Fx0)+3(fx1)+3(fx2)+(fx3))

# se calcula h para la formula
h= (limite_superior-limite_inferior)/n  # (a-b) /n  recordando que n=3
# se calculan x0,x1,x2,x3 con las sigueientes formulas
x0= limite_inferior #x0=b
x1=x0+h #b+h
x2=x1+h 
x3=x2+h 
# ya calculadas las x, calculamos las fx usando la funcion
fx0= funcion(x0)
fx1=funcion(x1)
fx2=funcion(x2)
fx3=funcion(x3)
# ya tenemos todo lo necesario para sustituirlo en la formula de la linea 14

resultado= (3/8)*(h)*((fx0)+3*(fx1)+3*(fx2)+(fx3))

#///////////////////////////////////

def reglaSimpson(a, b, n):
    resultado = 0
    sumatoria = 0
    Delta = ((b-a)/n)
    for i in range(n+1):
        xi = (a + (i*Delta))
        # funcion
        funcion = log(xi-tan(np.e**(2*xi)))
        if xi == a or xi == b:
            sumatoria += funcion
        elif i % 2 != 0:
            funcion = 4*funcion
            sumatoria += funcion
        elif i % 2 == 0:
            funcion = 2*funcion
            sumatoria += funcion
        
    resultado = (Delta/3)*sumatoria

    return resultado
    
print ('Universidad de las Fuerzas Armadas ESPE-L')
print ('Metodos de integracion numerica/n')

print ('Ejercicio 1')

limitex0=float(input("Escriba el limite inferior: "))
limitex1=float(input("Escriba el limite superior: "))

xi = [0,0.12,0.24,0.36,0.48,0.6,0.72,0.84,0.96,1.08,1.2,1.32,1.44,1.56,1.68,1.8,1.92,2.04,2.16,2.28]
fi = [1.20,10.51,3.60,5.71,5.41,1.80,1.80,0.60,0.60,3.90,0.90,9.61,3.00,9.91,9.01,8.71,10.51,8.71,8.11,9.61]

h=(limitex1-limitex0)/3

Resultado=((3*(h))/8)*(fi[16]+(3*fi[17])*(3*fi[18])+(fi[19]))
print(Resultado)

Resultado2=((1/3)*h)*((fi[0]+4*(((fi[1])+2)+((fi[3])+2)+((fi[5])+2)+((fi[7])+2)+((fi[9])+2)+((fi[11])+2)+((fi[13])+2)+((fi[15])+2)+((fi[17])+2)+((fi[19])+2)))+(2*(((fi[2])+fi[19])+((fi[4])+fi[19])+((fi[6])+fi[19])+((fi[8])+fi[19])+((fi[10])+fi[19])+((fi[12])+fi[19])+((fi[14])+fi[19])+((fi[16])+fi[19])+((fi[18])+fi[19]))))

Recorrido=Resultado2+Resultado
print("El recorrido hecho por la particula es: ",Recorrido," m")
print ('Ejercicio 2')
print("El resultado en 3 subintervalos es: ",resultado)
print( "El resultado de la integral  para 2 sub intervalos es:", reglaSimpson(2, 2.5, 2))
print( "El resultado de la integral  para 10 sub intervalos es:", reglaSimpson(2, 2.5, 10))
print( "El resultado de la integral  para 17 sub intervalos es:", reglaSimpson(2, 2.5, 14)+resultado)

