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

def newtonRaphson (func , x0 , numIt , tolera):
    derfx =str(diff(func, x))

    x1 = x0
    it = 0 
    error = 0
    # Creacion matriz 
    m_itera=np.array([]) #matriz q almacena valores de itera
    m_x0=np.array([])   #matriz q alamacena valores de xl
    m_x1=np.array([])   #matriz q alamcena valores de xu
    m_error=np.array([])   #matriz q almacena valroes de xr

    while it < numIt or error < tolera :
        it +=1
        libres=dict(x=x1) 
        funcs = vars(math)
        fx = eval(func, funcs,libres)

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

def secante(func, x1, x2):

    # Creacion matriz 
    m_itera=np.array([]) #matriz q almacena valores de itera
    m_x1=np.array([])   #matriz q alamacena valores de xl
    m_x2=np.array([])   #matriz q alamcena valores de xu
    m_x3=np.array([])   #matriz q almacena valroes de xr
    m_ea=np.array([])   #matriz q alamcena valore s de ea

    error = 0
    it = 0
    while  it < 8  :
        it += 1
        libres=dict(x=x1) 
        funcs = vars(math)
        fx1 = eval(func, funcs,libres)

        libres=dict(x=x2)  
        funcs = vars(math)
        fx2 = eval(func, funcs,libres)

        x3 = (x2*fx1 - x1*fx2) / (fx1-fx2)
        error = abs((x3-x2)/x3)*100
       
        #agregamos valores a las matrices vacias
        m_itera=np.append(m_itera,it)
        m_x1=np.append(m_x1,x1)
        m_x2=np.append(m_x2,x2)
        m_x3=np.append(m_x3,x3)
        m_ea=np.append(m_ea,error)    

        x1 = x2
        x2 = x3

        #representamos datos en pandas
    iteracion=pd.Series(m_itera,name="Iteracion")
    x1=pd.Series(m_x1,name="x1")
    x2=pd.Series(m_x2,name="x2")
    x3=pd.Series(m_x3,name="x3")
    ea=pd.Series(m_ea,name="ea%")
    tabla=pd.concat([iteracion,x1,x2, x3,ea],axis=1) #unimos en columnas
    return tabla


Eopcion=str('si')
while Eopcion=='si' or Eopcion=='Si' or Eopcion=='SI':
   
    print("Elija el metodo por el cual quiere encontrar la raiz: ")
    print("1.Metodo Punto Fijo")
    print("2.Metodo Newton Raphson")
    print("3.Metodo de la Secante")
    print("3.Salir")
    
    elegir = int(input())
    
    if (elegir == 1 ):
        limiteInf = float (input('Digite el limite inferior xl: '))
        limiteSup = float (input('Digite el limite superior xu: '))
        numIteracion = float (input('Digite el maximo de iteraciones: '))
        tolera = float (input('Digite menor a cuanto quiere el error: '))
        a=puntoFijo(x,func,limiteInf,limiteSup, numIteracion , tolera)
        print (a)
    elif (elegir == 2):
        limiteInf = float (input('Digite el limite inferior xl: '))
        numIteracion = float (input('Digite el maximo de iteraciones: '))
        tolera = float (input('Digite menor a cuanto quiere el error: '))

        c = newtonRaphson (func ,limiteInf, numIteracion , tolera)
        print (c)
    elif (elegir == 3 ):
        x1 = float (input('Digite el punto x1: '))
        x2 = float (input('Digite el punto x2: '))
        d = secante (func, x1 , x2 )
        print (d)

    Eopcion = input('Desea continuar: ')