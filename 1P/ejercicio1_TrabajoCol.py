import math
import pandas as pd
import numpy as np
from sympy import *
from sympy.parsing import sympy_parser


x = Symbol('x') #declaramos que x es un simbolo
print("\t\t\tUNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE-L\n")
print ('Metodos Abiertos')
func = input ('Ingrese la funcion:')#funcion que evaluaremos

#metodo de la biseccion
def Bisec(func,xl,xu,emax):
    itera=0 
    xr=0
    ea = 100
    m_itera=np.array([]) #matriz q almacena valores de itera
    m_xl=np.array([])   #matriz q alamacena valores de xl
    m_xu=np.array([])   #matriz q alamcena valores de xu
    m_xr=np.array([])   #matriz q almacena valroes de xr
    m_ea=np.array([])   #matriz q alamcena valore s de ea
    fl = dict (x=xl)
    funcs = vars(math)
    fll = eval (func, funcs, fl)
    #fl=func.evalf(subs={x: xl}) #reamplazmos x por xl y evaluamos la funcion
    #incio del bucle
    while ea>emax :
        
        xanterior=xr
        xr=(xl+xu)/2   # Fórmula de la BISECCIÓN
        fr = dict (x = xr)
        funcs = vars(math)
        frr = eval(func, funcs, fr)
        #fr=func.evalf(subs={x:xr})
        itera=itera+1
        
        if xr != 0:
            ea=abs((xr-xanterior)/xr)*100
            
        signo=fll*frr
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
            fll=frr
        else:
            ea=0
            
    #representamos datos en pandas
    iteracion=pd.Series(m_itera,name="Iteracion")
    xl=pd.Series(m_xl,name="xl")
    xu=pd.Series(m_xu,name="xu")
    xr=pd.Series(m_xr,name="xr")
    ea=pd.Series(m_ea,name="ea%")
    tabla=pd.concat([iteracion,xl,xu,xr,ea],axis=1) #unimos en columnasno   

    return tabla 

def puntoFijo (x,func , a , b , tolera, iteramax ):

    nuevaFunc = (sympy_parser.parse_expr(func)) #transforma func de str a Sympy (funcion)
    op = nuevaFunc + x #Suma x en la funcion 
    func = str(op)

    print ('funcion ya sumada x: ' ,func)
    
    i = 0 # iteración
    fx = dict (x = a)
    funcs = vars(math)
    fxa = eval(func, funcs, fx)

    b = fxa
    tramo = abs(b-a)
    while(tramo>=tolera and i<=iteramax ):
        a = b
        fx = dict (x = a)
        funcs = vars(math)
        fxa = eval(func, funcs, fx)
        b = fxa
        tramo = abs(b-a)
        i = i + 1
    respuesta = b
    
    # Validar respuesta
    if (i>=iteramax ):
        respuesta = np.nan
        print('La funcion diverge')
    return(respuesta, tramo, i)

Eopcion=str('si')
while Eopcion=='si' or Eopcion=='Si' or Eopcion=='SI':
   
    print("Elija el metodo por el cual quiere encontrar la raiz: ")
    print("1.Metodo biseccion")
    print("2.Metodo Punto Fijo")
    print("3.Salir")
    
    elegir = int(input())
    
    if (elegir == 1 ):
        limiteInf = float (input('Digite el limite inferior xl: '))
        limiteSup = float (input('Digite el limite superior xu: '))
        errorDes = float (input('Digite menor a cuanto quiere el error: '))
        
        a=Bisec(func,limiteInf,limiteSup,errorDes)
        print (a)
    elif (elegir == 2 ):
        limiteInf = float (input('Digite el limite inferior xl: '))
        limiteSup = float (input('Digite el limite superior xu: '))
        numIteracion = float (input('Digite el maximo de iteraciones: '))
        tolera = float (input('Digite menor a cuanto quiere el error: '))
        a=puntoFijo(x,func,limiteInf,limiteSup, numIteracion , tolera)
        print (a)
        
    Eopcion = input('Desea continuar: ')