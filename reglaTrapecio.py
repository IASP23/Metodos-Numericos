# Integración: Regla de los trapecios
from email.policy import default
from matplotlib import transforms
import numpy as np
import matplotlib.pyplot as plt
from sympy import * 
from dill.source import getsource

# INGRESO
fx = lambda x: np.sqrt(x)*np.sin(x)

# intervalo de integración
a = 1
b = 3
tramos = 4

print ('\tUniversidad de las Fuerzas Armadas ESPE-L\n')
print ('Metodos de integracion numerica')
print ('Metodo del trapecio')
# PROCEDIMIENTO
# Puntos de muestra
def reglaTrapecio (a, b , tramos):
    muestras = tramos + 1
    xi = np.linspace(a,b,muestras)
    fi = fx(xi)

    # Regla del Trapecio
    # Usando puntos muestreados
    # incluso arbitrariamente espaciados
    suma = 0
    for i in range(0,tramos,1):
        dx = xi[i+1]-xi[i]
        Atrapecio = dx*(fi[i]+fi[i+1])/2
        suma = suma + Atrapecio
    integral = suma

    # SALIDA
    print (dx)
    print('tramos: ', tramos)
    print('integral: ', integral)
    # GRAFICA
    # Puntos de muestra
    muestras = tramos + 1
    xi = np.linspace(a,b,muestras)
    fi = fx(xi)
    # Linea suave
    muestraslinea = tramos*10 + 1
    xk = np.linspace(a,b,muestraslinea)
    fk = fx(xk)

    # Graficando
    plt.plot(xk,fk, label ='f(x)')
    plt.plot(xi,fi, marker='o',
            color='orange', label ='muestras')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Integral: Regla de Trapecios')
    plt.legend()

    # Trapecios
    plt.fill_between(xi,0,fi, color='g')
    for i in range(0,muestras,1):
        plt.axvline(xi[i], color='w')

    plt.show()

print (reglaTrapecio (a, b , tramos))