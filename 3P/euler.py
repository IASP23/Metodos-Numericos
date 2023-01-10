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
yo = float(input('Ingrese el valor inicial'))
h = (b-a)/n
t = np.zeros(n+1)
y = np.zeros(n+1)
yex = np.zeros(n+1)
t[0] = a
y[0] = yo
yex[0] = yo
for i in np.arange(0,n):
    #print('y = ', y[i] ,'+', h ,'*' ,funcion(t[i], y[i] ,'=',y[i] ))
    y[i+1] = y[i] + h * (funcion(t[i], y[i]))
    #yex[i+1] = solucion(t[i])
    t[i+1] = t[i] + h
    print ('i=',i)
    print('y=', y[i] ,'+', h ,'*' ,funcion(t[i], y[i] ),'=',y[i],'\n')

print(t)
print(y)
plt.scatter(t,y)
plt.scatter(t,yex)

def funcion (t,y):
    y=0
    ec = (-2.470091*t*t*y)/2+24.950910*t
    return (ec)

a = float(input('Ingrese el tiempo inicial'))
b = float(input('Ingrese el tiempo final'))
n = int(input('Ingrese número de subintervalos'))
yo = float(input('Ingrese el valor inicial'))
h = (b-a)/n
t = np.zeros(n+1)
y = np.zeros(n+1)
yex = np.zeros(n+1)
t[0] = a
y[0] = yo
yex[0] = yo
for i in np.arange(0,n):
    y[i+1] = y[i] + h * (funcion(t[i], y[i]))
    #yex[i+1] = solucion(t[i])
    t[i+1] = t[i] + h
print(t)
print(y)
plt.scatter(t,y)
plt.scatter(t,yex)

