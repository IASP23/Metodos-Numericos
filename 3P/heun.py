# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 07:05:09 2022

@author: ASUS I7 10MA
"""
import numpy as np
import matplotlib.pyplot as plt
import math as mh
import pandas as pd

def funcion (t,y):
    ec = -2.470091
    return (ec)

a = float(input('Ingrese el tiempo inicial'))
b = float(input('Ingrese el tiempo final'))
n = int(input('Ingrese número de subintervalos'))
yo = int(input('Ingrese el valor inicial'))
h = (b-a)/n
t = np.zeros(n+1)
y = np.zeros(n+1)
yex = np.zeros(n+1)
t[0] = a
y[0] = yo
yex[0] = yo
for i in np.arange(0,n):
    yp = y[i] + h * (funcion(t[i], y[i]))
    print ('i=',i)
    print ('y*=',y[i],'+',h,'*',(funcion(t[i], y[i])))
    y[i+1] = y[i] +( h * ((funcion(t[i], y[i]))+(funcion(t[i]+h, yp)))/2)
    print('y=', y[i] ,'+(', h ,'*', (funcion(t[i], y[i])),'+',(funcion(t[i]+h, yp)),'/',2,')=', y[i+1])
  #  yex[i+1] = solucion(t[i])
    t[i+1] = t[i] + h
print(t)
print(y)
plt.scatter(t,y)
#plt.scatter(t,yex)


