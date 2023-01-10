import math
from os import error
import pandas as pd
import numpy as np
from sympy import *

x = Symbol('x') #declaramos que x es un simbolo
print("\t\t\tUNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE-L\n")
print ('Metodos Abiertos')
func = input ('Ingrese la funcion:')#funcion que evaluaremos
delta = 0.001
seleccion = 0
while (seleccion ==0):
    
    x1 = float(input('Digite el valor a evaluar:'))
    libres=dict(x=x1) 
    funcs = vars(math)
    fx1 = eval(func, funcs,libres)
    print (fx1)

    op = 0.001*(x1)
    print ('0.001 * x1 = ' , op)
    x2= x1 + op
    print (x2)
    libres=dict(x=x2) 
    funcs = vars(math)
    fx2 = eval(func, funcs,libres)

    print(fx2)
    
    resultado = x1  - (op*fx1)/(fx2-fx1)
    print (resultado)
    seleccion = int (input('Dijite 0 para continuar: '))
