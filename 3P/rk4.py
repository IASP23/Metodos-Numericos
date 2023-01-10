import numpy as np
from sympy import *
from numpy import log as ln
import math

def f(t , y): #aquí va la funcion a evaluar
    res = y*t**2 - y 
    return res

h = 0.25
t = 0 
tfin = 0.75
y= 1
aux = 0 
i = 0 
while t <= tfin :
    k1 = h*f(t,y)
    print ('K1: ',k1)
    k2 = h * f (t +h/2 , y + k1/2)
    print ('K2: ',k2)
    k3 = h * f (t +h/2 , y + k2/2)
    print ('K3: ',k3)
    k4 = h*f(t+h , y+k3) 
    print ('K4: ',k4)
    ynuevo = y + (k1+2*k2+2*k3+k4)/6 
    print ('Y: ',ynuevo)
    print ('yo soy y anterior:',y)
    t+=h 
    y = aux 
    aux = ynuevo 
    y = ynuevo
