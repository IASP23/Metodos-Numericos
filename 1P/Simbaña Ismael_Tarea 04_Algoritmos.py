import math
from os import error
import pandas as pd
import numpy as np
from sympy import *

x = Symbol('x') #declaramos que x es un simbolo
print("\t\t\tUNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE-L\n")
print ('Metodos Abiertos')
func = input ('Ingrese la funcion:')#funcion que evaluaremos

def Bisec(func,xl,xu):
    it=0 
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
    print('Funcion evaluala en ', xl , 'es' , fll)
    fx = dict (x=xu)
    funcs = vars(math)
    fxu = eval (func, funcs, fx)
    print('Funcion evaluala en ', xu , 'es' , fxu)
    while it < 15 :
        
        xanterior=xr
        xr=(xl+xu)/2  
        fr = dict (x = xr)
        funcs = vars(math)
        frr = eval(func, funcs, fr)
        it +=1
        if xr != 0:
            ea=abs((xr-xanterior)/xr)*100
        print('Funcion evaluala en ', xr , 'es' , frr)
        signo=fll*frr
        #agregamos valores a las matrices vacias
        m_itera=np.append(m_itera,it)
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
    tabla=pd.concat([iteracion,xl,xu,xr,ea],axis=1) #unimos en columnas

    print(tabla) 

def reglaFalsa(func,xl , xu ):

    it=0 
    xr = 0
    m_itera=np.array([]) #matriz q almacena valores de itera
    m_xl=np.array([])   #matriz q alamacena valores de xl
    m_xu=np.array([])   #matriz q alamcena valores de xu
    m_xr=np.array([])   #matriz q almacena valroes de xr

    m_ea=np.array([])   #matriz q alamcena valore s de ea
    
    libres=dict(x=xu) #evalua en b
    funcs = vars(math)
    fb = eval(func, funcs,libres)
        	
    libres=dict(x=xl) #evalua en a
    funcs = vars(math)
    fa=eval(func, funcs,libres)
    	
    #incio del bucle
    while   (it < 8 ) :
        it+=1
        xanterior = xr
        xr = xu - fb*(xl-xu)/(fa-fb)
    	    	
        libres=dict(x=xr) #evalua en xr
        funcs = vars(math)
        fxr=eval(func, funcs,libres)	

        verdaError = abs ((xr-xanterior))/xr *100
                #agregamos valores a las matrices vacias
        m_itera=np.append(m_itera,it)
        m_xl=np.append(m_xl,xl)
        m_xu=np.append(m_xu,xu)
        m_xr=np.append(m_xr,xr)

        m_ea=np.append(m_ea,verdaError)   
        print(it,'---------------------------------')
        print(xu,'*', fa, -xl,'*', fb)
        print(fa,'-',fb)
        print('=', xr)

        print ('e=', xr,'-', xanterior )
        print('---------------------------------')
        
        n_x = np.sign(fa)*np.sign(fxr)
        
        if n_x>0:
            xl=xr
            fa = fxr
        else :
            xu=xr
            fb = fxr 
                  
     #representamos datos en pandas
    iteracion=pd.Series(m_itera,name="Iteracion")
    xl=pd.Series(m_xl,name="xl")
    xu=pd.Series(m_xu,name="xu")
    xr=pd.Series(m_xr,name="xr") 
    ea=pd.Series(m_ea,name="ea%")
    tabla=pd.concat([iteracion,xl,xu,xr,  ea],axis=1) #unimos en columnas
    print(tabla) 

def newtonRaphson (func , x0):
    derfx =str(diff(func, x))

    x1 = x0
    it = 0 

    # Creacion matriz 
    m_itera=np.array([]) #matriz q almacena valores de itera
    m_x0=np.array([])   #matriz q alamacena valores de xl
    m_x1=np.array([])   #matriz q alamcena valores de xu
    m_error=np.array([])   #matriz q almacena valroes de xr

    while it <= 5:
        it +=1
       
        libres=dict(x=x1) 
        funcs = vars(math)
        fx = eval(func, funcs,libres)

        libres=dict(x=x1) 
        funcs = vars(math)
        dfx = eval(derfx, funcs,libres)

        xnuevo = x1 - fx/dfx
        error  = abs((xnuevo-x1)/xnuevo)*100
        x0=x1
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
    return (tabla) 

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
        print (it, '----------------------------------------') 
        print (x2, fx1 , '-' , x1 , fx2)
        print (fx1 , '-'  ,fx2)
        print (x3)

        print ('error' , x3 - x2 , error)
        print (it, '----------------------------------------') 


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
    print(tabla) 

def muller (func , x0, x1 , x2 ):
    error = 1e3
    x3 = 0
    it = 0 

        # Creacion matriz 
    m_itera=np.array([]) #matriz q almacena valores de itera
    m_x0=np.array([])   #matriz q alamacena valores de xl
    m_x1=np.array([])   #matriz q alamcena valores de xu
    m_x2=np.array([])   #matriz q almacena valroes de xr
    m_ea=np.array([])   #matriz q alamcena valore s de ea
 

    while it < 8 :
        
        libres=dict(x=x2) 
        funcs = vars(math)
        fx2 = eval(func, funcs,libres)

        libres=dict(x=x1) 
        funcs = vars(math)
        fx1 = eval(func, funcs,libres)

        libres=dict(x=x0) 
        funcs = vars(math)
        fx0 = eval(func, funcs,libres)
        print (it, '=========================================')
        print ('fx0 = ' , x0 ,'=' , fx0)
        print ('fx1 = ' , x1 ,'=' , fx1)
        print ('fx2 = ' , x2 ,'=' , fx2)
        h0 = x1-x0
        print ('h0=' ,x1  , '-' , x0)
        h1 = x2-x1
        print ('h1=' ,x2  , '-' , x1)

        d0 = (fx1-fx0)/h0   
        print ('d0=', fx1 ,'-',fx0, '/', h0)
        d1 = (fx2-fx1)/h1
        print ('d1=', fx2 ,'-',fx1, '/', h1)

        a= (d1-d0)/(h1+h0)
        print ('a=',d1,'-',d0,'/',h1,'+',h0)
        b= a*h1+d1
        print('b=',a,'*',h1,'+',d1)
        c = fx2
        print ('c=',fx2)

        x3 = x2 - (2 * c) / (b + np.sign(b) * np.sqrt(b**2 - 4 * a * c))
        error = abs((x3 - x2)/x3)*100
        
                #agregamos valores a las matrices vacias
        m_itera=np.append(m_itera,it)
        m_x0=np.append(m_x0,x0)
        m_x1=np.append(m_x1,x1)
        m_x2=np.append(m_x2,x2)
        m_ea=np.append(m_ea,error)    

        x0 = x1
        x1 = x2
        x2 = x3
        it +=1
            #representamos datos en pandas
    iteracion=pd.Series(m_itera,name="Iteracion")
    x1=pd.Series(m_x0,name="x1")
    x2=pd.Series(m_x1,name="x2")
    x3=pd.Series(m_x2,name="x3")
    ea=pd.Series(m_ea,name="ea%")
    tabla=pd.concat([iteracion,x1,x2, x3,ea],axis=1) #unimos en columnas
    print(tabla) 


Eopcion=str('si')

while Eopcion=='si' or Eopcion=='Si' or Eopcion=='SI':

    print("Elija el metodo por el cual quiere encontrar la raiz: ")
    print("1.Metodo de la Bisección")
    print("2.Metodo de la Regla Falsa")
    print("3.Metodo Newton Raphson")
    print("4.Metodo de la Secante")
    print("5.Metodo de Muller")
    print("6.Salir")
    
    elegir = int(input())
    
    if (elegir == 1 ):
        limiteInf = float (input('Digite el limite inferior xl: '))
        limiteSup = float (input('Digite el limite superior xu: '))
        
        a=Bisec(func,limiteInf,limiteSup)
        print (a)
        
    elif (elegir ==2):      
        limiteInf = float (input('Digite el limite inferior xl: '))
        limiteSup = float (input('Digite el limite superior xu: '))
        
        b=reglaFalsa(func,limiteInf,limiteSup)
        print (b)
    elif (elegir == 3):
        limiteInf = float (input('Digite el limite inferior xl: '))
        c = newtonRaphson (func ,limiteInf)
        print (c)
    elif (elegir == 4 ):
        x1 = float (input('Digite el punto x1: '))
        x2 = float (input('Digite el punto x2: '))
        d = secante (func, x1 , x2 )
        print (d)
    elif (elegir == 5 ):
        x0 = float (input('Digite x0: '))
        x1 = float (input('Digite x1: '))
        x2 = float (input('Digite x2: '))


        e= muller (func, x0 , x1 , x2 )
       
    else:
        print('A finalizado el programa para calcular raices mediante metodos')
        break
    
    Eopcion = input('Desea continuar: ')