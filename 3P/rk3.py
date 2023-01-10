import numpy as np
from sympy import *
from numpy import log as ln
import math

def f(t , y): #aquí va la funcion a evaluar
    res = t-y
    return res

h = 0.1
t = 0
tfin = 1
y= 2
aux = 0 

while t <= tfin :
    k1 = h*f(t,y)
    print ('K1: ',k1)
    k2 = h * f (t +h/2 , y + k1/2)
    print ('K2: ',k2)
    k3 = h * f (t +h, y-k1+ 2*k2)
    print ('K3: ',k3)
    ynuevo = y + (k1+4*k2+k3)/6
    print ('Y: ',ynuevo)
    print ('yo soy y anterior:',y)
    t+=h 
    y = aux 
    aux = ynuevo 
    y = ynuevo
