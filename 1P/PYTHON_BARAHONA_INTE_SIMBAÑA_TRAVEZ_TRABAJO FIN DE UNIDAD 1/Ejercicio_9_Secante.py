# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:43:50 2021

@author: Juan
"""

import matplotlib.pyplot as plt
import numpy as np

def secante_tabla(fx,xa,tolera):
    dx = 6*tolera
    xb = xa + dx
    tramo = dx
    tabla = []
    while (tramo>=tolera):
        fa = fx(xa)
        fb = fx(xb)
        xc = xa - fa*(xb-xa)/(fb-fa)
        tramo = ((abs(xc-xa))/xc)*100
        print("f(x0)",fx(xa))
        print("f(x1)",fx(xb))
        
        
        tabla.append([xa,xb,xc,tramo])
        xb = xa
        xa = xc

    tabla = np.array(tabla)
    return(tabla)

# PROGRAMA ---------------------
# INGRESO
fx = lambda x: 4.5080*10**(-5)*x**(2)-0.1470*x-11.973 

a  = 3340.3
b  = 3340.5
xa = 3340.4
tolera = 0.00001
tramos = 100

# PROCEDIMIENTO
tabla = secante_tabla(fx,xa,tolera)
n = len(tabla)
raiz = tabla[n-1,2]

# SALIDA
np.set_printoptions(precision=6)
print('[xa ,\t xb , \t xi+1 , \t tramo]')
for i in range(0,n,1):
    print(tabla[i])
print('raiz en: ', raiz)

# Calcula los puntos a graficar
xi = np.linspace(a,b,tramos+1)
fi = fx(xi)
dx = (b-xa)/2
pendiente = (fx(xa+dx)-fx(xa))/(xa+dx-xa)
b0 = fx(xa) - pendiente*xa
tangentei = pendiente*xi+b0

fxa = fx(xa)
xb = xa + dx
fxb = fx(xb)

plt.plot(xi,fi, label='f(x)')

plt.plot(xi,tangentei, label='secante')
plt.plot(xa,fx(xa),'go', label='xa')
plt.plot(xa+dx,fx(xa+dx),'ro', label='xb')
plt.plot((-b0/pendiente),0,'yo', label='xc')

plt.plot([xa,xa],[0,fxa],'m')
plt.plot([xb,xb],[0,fxb],'m')

plt.axhline(0, color='k')
plt.title('Método de la Secante')
plt.legend()
plt.grid()
plt.show()