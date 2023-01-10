import pandas as pd
import numpy as np
from sympy import *
from math import *

x = Symbol('x')
fx = lambda x: 2000 * ln(1 + 2700 * x) * 9.81 * x - 750 
dfx = lambda x: 5400000/2700*x - 9.81
a = 10
b = 50
tolera = 0.001

opcion = 0
def menu():
    opc = int(input('Menu Principal \n '+
                    '1.Método Biseccion \n'+
                    '2.Método de la Regla falsa \n'+
                    '3.Newton - Rapshon \n'+
                    '4.Secante \n'+
                    '5.Müller \n'+
                    '6.Finalizar \n' + 
                    'Elija una Opcion : \n'))
    return opc
def Bisec(xl,xu,emax):
    x = Symbol('x') #declaramos que x es un simbolo
    func = 2000 * ln(1 + 2700 * x) * 9.81 * x - 750
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
        elif signo > 0:
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


def newRap(fx,dfx,x0,tolera):
    tabla = []
    tramo = abs(2*tolera)
    xi = x0
    while (tramo>=tolera):
        xnuevo = xi - fx(xi)/dfx(xi)
        tramo  = abs(xnuevo-xi)
        tabla.append([xi,xnuevo,tramo])
        xi = xnuevo
    
    tabla = np.array(tabla)
    n = len(tabla)
    
   
    print(['xi', 'xnuevo', 'tramo'])
    np.set_printoptions(precision = 4)
    print(tabla)
    print('raiz en: ', xi)
    print('con error de: ',tramo)
    
def muller(fx):
    i=0
    x0=0
    x=x0
    f0=fx
    x1=10
    x=x1
    f1=fx
    x2=50
    x=x2
    f2=fx
    h0=x1-x0
    h1=x2-x1
    d0=(f1-f0)/h0
    d1=(f2-f1)/h1
    a=(d1-d0)/(h1+h0)
    b=a*h1+d1
    c=f2
    print("i x0     x1     x2     f0      f1      f2      h0      h1     d0      d1      a       b       c     ")
    print(str(i) + " {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f}".format(x0,x1,x2,f0,f1,f2,h0,h1,d0,d1,a,b,c))
    if b>0:
        x3=x2-2*c/(b+(b**2-4*c*a)**0.5)
    else:
        x3=x2-2*c/(b-(b**2-4*c*a)**0.5)
    print("x3 = " + "{:.4f}".format(x3))
    print("---------------------------------------")
    
    i=1
    x0=x1
    x=x0
    f0=fx
    x1=x2
    x=x1
    f1=fx
    x2=x3
    x=x2
    f2=fx
    h0=x1-x0
    h1=x2-x1
    d0=(f1-f0)/h0
    d1=(f2-f1)/h1
    a=(d1-d0)/(h1+h0)
    b=a*h1+d1
    c=f2
    print("i x0     x1     x2     f0      f1      f2      h0      h1     d0      d1      a       b       c     ")
    print(str(i) + " {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f}".format(x0,x1,x2,f0,f1,f2,h0,h1,d0,d1,a,b,c))
    if b>0:
        x3=x2-2*c/(b+(b**2-4*c*a)**0.5)
    else:
        x3=x2-2*c/(b-(b**2-4*c*a)**0.5)
    print("x3 = " + "{:.4f}".format(x3))
    
    print("---------------------------------------")
    
    i=2
    x0=x1
    x=x0
    f0=fx
    x1=x2
    x=x1
    f1=fx
    x2=x3
    x=x2
    f2=fx
    h0=x1-x0
    h1=x2-x1
    d0=(f1-f0)/h0
    d1=(f2-f1)/h1
    a=(d1-d0)/(h1+h0)
    b=a*h1+d1
    c=f2
    print("i x0     x1     x2     f0      f1      f2      h0      h1     d0      d1      a       b       c     ")
    print(str(i) + " {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f}".format(x0,x1,x2,f0,f1,f2,h0,h1,d0,d1,a,b,c))
    if b>0:
        x3=x2-2*c/(b+(b**2-4*c*a)**0.5)
    else:
        x3=x2-2*c/(b-(b**2-4*c*a)**0.5)
    print("x3 = " + "{:.4f}".format(x3))
    print("---------------------------------------")
    
    i=3
    x0=x1
    x=x0
    f0=fx
    x1=x2
    x=x1
    f1=fx
    x2=x3
    x=x2
    f2=fx
    h0=x1-x0
    h1=x2-x1
    d0=(f1-f0)/h0
    d1=(f2-f1)/h1
    a=(d1-d0)/(h1+h0)
    b=a*h1+d1
    c=f2
    print("i x0     x1     x2     f0      f1      f2      h0      h1     d0      d1      a       b       c     ")
    print(str(i) + " {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f}".format(x0,x1,x2,f0,f1,f2,h0,h1,d0,d1,a,b,c))
    if b>0:
        x3=x2-2*c/(b+(b**2-4*c*a)**0.5)
    else:
        x3=x2-2*c/(b-(b**2-4*c*a)**0.5)
    print("x3 = " + "{:.4f}".format(x3))
def secante_tabla(fx,xa,tolera):
    dx = 4*tolera
    xb = xa + dx
    tramo = dx
    tabla = []
    while (tramo>=tolera):
        fa = fx(xa)
        fb = fx(xb)
        xc = xa - fa*(xb-xa)/(fb-fa)
        tramo = abs(xc-xa)
        
        tabla.append([xa,xb,xc,tramo])
        xb = xa
        xa = xc

    tabla = np.array(tabla)
    return(tabla)
         
while opcion != 6:
    opcion = menu()
    
    if opcion ==1:
        a=Bisec(10,50,0.001)
        print(a)
    
    if opcion == 2:
        tabla = []
        tramo = abs(b-a)
        fa = fx(a)
        fb = fx(b)
        while not(tramo<=tolera):
            c = b - fb*(a-b)/(fa-fb)
            fc = fx(c)
            tabla.append([a,c,b,fa,fc,fb,tramo])
            cambio = np.sign(fa)*np.sign(fc)
            if cambio>0:
                tramo = abs(c-a)
                a = c
                fa = fc
            else:
                tramo = abs(b-c)
                b = c
                fb = fc
                
        tabla = np.array(tabla)
        ntabla = len(tabla)
        
        np.set_printoptions(precision=4)
        for i in range(0,ntabla,1):
            print('iteración:  ',i)
            print('[a,c,b]:    ', tabla[i,0:3])
            print('[fa,fc,fb]: ', tabla[i,3:6])
            print('[tramo]:    ', tabla[i,6])
        
        print('raiz:  ',c)
        print('error: ',tramo)
        
    if opcion == 3:
       x0 = 50
    tolera = 0.001
    
    tabla = []
    tramo = abs(2*tolera)
    xi = x0
    while (tramo <= tolera):
        xnuevo = xi - fx(xi)/dfx(xi)
        tramo  = abs(xnuevo-xi)
        tabla.append([xi,xnuevo,tramo])
        xi = xnuevo
    
  
    tabla = np.array(tabla)
    n = len(tabla)
    

    print(['xi', 'xnuevo', 'tramo'])
    np.set_printoptions(precision = 4)
    print(tabla)
    print('raiz en: ', xi)
    print('con error de: ',tramo)
        
    if opcion == 4:
        tabla = secante_tabla(fx,a,tolera)
        n = len(tabla)
        raiz = tabla[n-1,2]
        
        np.set_printoptions(precision=4)
        print('[xa ,\t xb , \t xc , \t tramo]')
        for i in range(0,n,1):
            print(tabla[i])
        print('raiz en: ', raiz)
        
    if opcion == 5:
        a=Bisec(45,50,0.001)
        print(a)
        
    if opcion ==6:
        print('El Sistema a finalizado correctamente')

