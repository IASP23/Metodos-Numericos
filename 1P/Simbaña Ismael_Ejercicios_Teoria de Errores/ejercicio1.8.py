import numpy as np
import math
import sympy as sym

x  = sym.Symbol('x')
fx = x - sym.sin(x)

x0 = 0
grado = 7      
n  = grado + 1  

k = 0 
polinomio = 0
while (k < n):
    derivada   = fx.diff(x,k)
    derx0 = derivada.subs(x,x0)
    divisor   = math.factorial(k)
    terminok  = (derx0/divisor)*(x-x0)**k
    polinomio += terminok
    k+=1

print('La serie de Taylor de la función f(x)=x-sen(x): ' ,polinomio)

#Evaluar  serie 
evaluarSerie = sym.sympify(polinomio).subs(x,0.1)
print ('La serie evaluada en 0.1: ', evaluarSerie)
