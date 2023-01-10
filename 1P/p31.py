import math
from sympy import *
from sympy import Symbol
from sympy.parsing import sympy_parser

x = Symbol('x') #declaramos que x es un simbolo
print("\t\t\tUNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE-L\n")
print ('Derivacion Numerica')
func = input ('Ingrese la funcion:')#funcion que evaluaremos

x1 = 1.5 
h = 0.1

libres=dict(x=x1) 
funcs = vars(math)
fx1 = eval(func, funcs,libres)

derfx =str(diff(func, x)) #Deriva la funcion principal
#Evalua la funcion derivada 
libres=dict(x=x1) 
funcs = vars(math)
funcionDerEva = eval(derfx, funcs,libres)


#hacia atras 

xmenosh = x - h 

libres=dict(x=xmenosh) 
funcs = vars(math)
fxmenosh = eval(func, funcs,libres)

fxatras = (fx1 -fxmenosh ) /  h 

errorAtras = abs ((funcionDerEva-fxatras)/funcionDerEva)*100
print ('Hacia atras: ',fxatras)
print ('Funcion derivada y evaluada: ',funcionDerEva)
print ('Error: ' , errorAtras, '%')

#centrada 
