# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:13:20 2021

@author: Juan
"""

import pandas as pd
import numpy as np


# INGRESO
fx  = lambda x: 4.5080*10**(-5)*x**(2)-0.1470*x-11.973 
dfx = lambda x: 0.00009016*x-0.147

x0 = 3340.5
tolera = 0.00001

# PROCEDIMIENTO
tabla = []
tramo = abs(2*tolera)
xi = x0
while (tramo>=tolera):
    xnuevo = xi - fx(xi)/dfx(xi)
    tramo  =( abs(xnuevo-xi)/xnuevo)*100
    tabla.append([xi,xnuevo,tramo])
    xi = xnuevo
    print("fx(x1)",fx(xi))
    print("dfx(x1)",dfx(xi))

# convierte la lista a un arreglo.
tabla = np.array(tabla)
n = len(tabla)

# SALIDA
print(['xi', 'xnuevo', 'tramo'])
np.set_printoptions(precision = 8)
print(tabla)
print('raiz en: ', xi)
print('con error de: ',tramo)