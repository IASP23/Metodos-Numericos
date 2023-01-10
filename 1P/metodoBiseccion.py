# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 05:38:22 2021

@author: ASUS I7 10MA
"""


import pandas as pd
import numpy as np
from sympy import *
from sympy.parsing import sympy_parser

x = Symbol('x') #declaramos que x es un simbolo
func = x*exp(-x/3)-0.7 #funcion que evaluaremos

print (type(func))
#metodo de la biseccion
def Bisec(func,xl,xu,emax):
    itera=0 
    m_itera=np.array([]) #matriz q almacena valores de itera
    m_xl=np.array([])   #matriz q alamacena valores de xl
    m_xu=np.array([])   #matriz q alamcena valores de xu
    xr=0
    m_xr=np.array([])   #matriz q almacena valroes de xr
    ea=100 
    m_ea=np.array([])   #matriz q alamcena valore s de ea
    fl=func.evalf(subs={x: xl}) #reamplazmos x por xl y evaluamos la funcion
    #incio del bucle
    while ea>emax :
        
        xanterior=xr
        xr=(xl+xu)/2   # Fórmula de la BISECCIÓN
        fr=func.evalf(subs={x:xr})
        itera=itera+1
        
        if xr != 0:
            ea=abs((xr-xanterior)/xr)*100
            
        signo=fl*fr
        #agregamos valores a las matrices vacias
        m_itera=np.append(m_itera,itera)
        m_xl=np.append(m_xl,xl)
        m_xu=np.append(m_xu,xu)
        m_xr=np.append(m_xr,xr)
        m_ea=np.append(m_ea,ea)                     
        
        if signo < 0 :
            xu=xr
        elif signo >0:
            xl=xr
            fl=fr
        else:
            ea=0
    #representamos datos en pandas
    iteracion=pd.Series(m_itera,name="Iteracion")
    xl=pd.Series(m_xl,name="xl")
    xu=pd.Series(m_xu,name="xu")
    xr=pd.Series(m_xr,name="xr")
    ea=pd.Series(m_ea,name="ea%")
    tabla=pd.concat([iteracion,xl,xu,xr,ea],axis=1) #unimos en columnas
    return tabla

a=Bisec(func,-1,5,0.0001)

print(a)
