import math
import pandas as pd
import numpy as np
from sympy import *

x = Symbol('x') #declaramos que x es un simbolo

def newtonRaphson (ux , x0):
    derfx =str(diff(ux, x))

    x1 = x0
    it = 0 
    error = 0
    # Creacion matriz 
    m_itera=np.array([]) #matriz q almacena valores de itera
    m_x0=np.array([])   #matriz q alamacena valores de xl
    m_x1=np.array([])   #matriz q alamcena valores de xu
    m_error=np.array([])   #matriz q almacena valroes de xr

    while it < 8 :
        it +=1
        libres=dict(x=x1) 
        funcs = vars(math)
        fx = eval(ux, funcs,libres)

        libres=dict(x=x1) 
        funcs = vars(math)
        dfx = eval(derfx, funcs,libres)

        xnuevo = x1 - fx/dfx
        error  = abs((xnuevo-x1)/xnuevo)*100
        x1 = xnuevo

        #agregamos valores a las matrices vacias
        m_itera=np.append(m_itera,it)
        m_x0=np.append(m_x0,x0)
        m_x1=np.append(m_x1,x1)
        m_error=np.append(m_error,error)  
    	
     #representamos datos en pandas
    iteracion=pd.Series(m_itera,name="Iteracion")
    x0=pd.Series(m_x0,name="xl")
    x1=pd.Series(m_x1,name="xu")
    ea=pd.Series(m_error,name="ea%")
    tabla=pd.concat([iteracion,x0,x1,ea],axis=1) #unimos en columnas
    return tabla

Eopcion=str('si')
while Eopcion=='si' or Eopcion=='Si' or Eopcion=='SI':
    print("\t\t\tUNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE-L\n")
    print("Metodo Newton Raphson con modificación")
    print('Ejercicio 10')
    ux = input ('Ingrese la funcion:')#funcion que evaluaremos
    limiteInf = float (input('Digite xi: '))
    
    c = newtonRaphson (ux ,limiteInf)
    print (c)

    Eopcion = input('Desea continuar (Si/No): ')