# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 09:20:10 2021

@author: Juan
"""

import math
import numpy as np
import matplotlib.pyplot as plt 


fx = lambda x: -1/120*E*I*L*W*(L**(4)-(6*L**(2)*x**(2))+5*(x**(4))) 
a = 260
b = 270
tolera = 0.00001
L=600
E=50000
I=30000
W=2.5

# PROCEDIMIENTO
tabla = []
tramo = b-a

fa = fx(a)
fb = fx(b)
i = 1
while (tramo>tolera):
    c = (a+b)/2
    fc = fx(c)
    tabla.append([i,   a,      c,      b,     fa,     fc,     fb,     tramo])
    i = i + 1
                 
    cambia = np.sign(fa)*np.sign(fc)
    if (cambia<0):
        b = c
        fb = fc
    else:
        a=c
        fa = fc
    tramo = b-a
c = (a+b)/2
fc = fx(c)
tabla.append([i,  a,c,b,fa,fc,fb,tramo])
tabla = np.array(tabla)

raiz = c

# SALIDA
np.set_printoptions(precision = 4)
print('[ i, a, c, b, f(a), f(c), f(b), tramo]')
# print(tabla)

# Tabla con formato
n=len(tabla)
for i in range(0,n,1):
    unafila = tabla[i]
    formato = '{:.0f}'+' '+(len(unafila)-1)*'{:.6f} '
    unafila = formato.format(*unafila)
    print(unafila)
    
print('raiz: ',raiz)

xi = tabla[:,2]
yi = tabla[:,5]

# ordena los puntos para la grafica
orden = np.argsort(xi)
xi = xi[orden]
yi = yi[orden]

plt.plot(xi,yi)
plt.plot(xi,yi,'o')
plt.axhline(0, color="black")

plt.xlabel('x')
plt.ylabel('y')
plt.title('EJERCICIO 6-Bisección en f(x)')
plt.grid()
plt.show()