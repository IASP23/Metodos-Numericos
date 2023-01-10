# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 13:51:02 2021

@author: Juan
"""

# Algoritmo Posicion Falsa para raices
# busca en intervalo [a,b]
# tolera = error

import numpy as np
import matplotlib.pyplot as plt

# INGRESO
fx = lambda x: 4.5080*10**(-5)*x**(2)-0.1470*x-11.973 

a = 3340.3
b = 3340.5
tolera = 0.00001

# PROCEDIMIENTO
tabla = []
tramo = abs(b-a)
fa = fx(a)
fb = fx(b)
while not(tramo<=tolera):
    c = b - fb*(a-b)/(fa-fb)
    fc = fx(c)
    tabla.append([a,c,b,fa,fc,fb,tramo])
    cambio = np.sign(fa)*np.sign(fc)
    if cambio>0:
        tramo = abs(c-a)
        a = c
        fa = fc
    else:
        tramo = abs(b-c)
        b = c
        fb = fc
        
tabla = np.array(tabla)
ntabla = len(tabla)

# SALIDA
np.set_printoptions(precision=6)
for i in range(0,ntabla,1):
    print('iteración:  ',i)
    print('[a,c,b]:    ', tabla[i,0:3])
    print('[fa,fc,fb]: ', tabla[i,3:6])
    print('[tramo]:    ', tabla[i,6])

print('raiz:  ',c)
print('error: ',tramo)