import numpy as np
from numpy import nan
from numpy.lib.type_check import nan_to_num
import math
import matplotlib.pyplot as plt

# PROCEDIMIENTO

# Gauss-Seidel
def gaussSeidel(A,B,X0,emax,itermax):

    m_error=np.array([]) #matriz q almacena valores de itera
    m_itera=np.array([])   #matriz q alamacena valores de xl

    dimension = np.shape(A)
    print (dimension)
    n = dimension[0]
    m = dimension[1]
    #  valores iniciales
    X = X0 
    print(X)
    diferencia = np.ones(n, dtype=float)
    print(diferencia)
    errado = 2*emax
    
    itera = 0
    while not(errado<=emax or itera>itermax):
        # por fila
        for i in range(0,n,1):
            # por columna
            suma = 0 
            for j in range(0,m,1):
                # excepto diagonal de A
                if (i!=j): 
                    suma = suma-A[i,j]*X[j]
            
            nuevo = (B[i]+suma)/A[i,i]
            diferencia[i] = np.abs(nuevo-X[i])
            X[i] = nuevo
        errado = np.max(diferencia)
        itera = itera + 1


        m_itera=np.append(m_itera,itera)
        m_error=np.append(m_error,errado)

    
        # revisa si NO converge
        if (itera>itermax):
            X=0
    plt.plot(m_itera , m_error)
    plt.show()

    return X
    # Respuesta X en columna
       

# INGRESO
def agregar_datos_matriz(filas, columnas):
    A = []

    for fil in range (filas):
        lista = []
        for col in range (columnas):
            print('Fila ' , fil , 'Columna' , col)
            dato = float(input())
            lista.append(dato)
        #Se crea una fila hasta aqui 
        A.append(lista)
    return A 


def gauss ():

    A = np.array([[4,2,5],
              [2,5,8],
              [5,4,3]])

    B = np.array([[60.70],
              [92.90],
              [56.30]])
    casicero = 1e-15 # Considerar como 0

    # Evitar truncamiento en operaciones
    A = np.array(A,dtype=float) 
    # Matriz aumentada
    AB  = np.concatenate((A,B),axis=1)
    AB0 = np.copy(AB)

    # Pivoteo parcial por filas
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]

    # Para cada fila en AB
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna  = abs(AB[i:,i])
        dondemax = np.argmax(columna)
        
        # dondemax no está en diagonal
        if (dondemax !=0):
            # intercambia filas
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
    AB1 = np.copy(AB)

    # eliminación hacia adelante
    for i in range(0,n-1,1):
        pivote   = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor  = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor

    # sustitución hacia atrás
    ultfila = n-1
    ultcolumna = m-1
    X = np.zeros(n,dtype=float)

    for i in range(ultfila,0-1,-1):
        suma = 0
        for j in range(i+1,ultcolumna,1):
            suma = suma + AB[i,j]*X[j]
        b = AB[i,ultcolumna]
        X[i] = (b-suma)/AB[i,i]

    X = np.transpose([X])


    # SALIDA
    print('Matriz aumentada:')
    print(AB0)
    print('Pivoteo parcial por filas')
    print(AB1)
    print('eliminación hacia adelante')
    print(AB)
    print('solución: ')
    a = np.array(X)
    print (np.isnan(a))# Verifica si existe algun valor no numerico
    #de ser asi vota un true
    print (X)
    x =  X.index(type(float))
    print ('valor',x)

    return nan 

def diagonalDominante (A):

    acum = 0 
    valoresP , vectoresP = np.linalg.eig(A)
    for i in range (len(A)):
        if (valoresP[i] >=0 ):
            acum += 1

    if (acum == len(A)):
        return True
    else :
        print ('Matriz de diagonal NO dominante')
        return False

# 1 
print ('Universidad de las Fuerzas Armadas ESPE-L ')
print ('Algoritmo de Gauss Seidel\n')

print('Cuantas filas')
filas = int (input())
print ('Cuantas columnas')
columnas = int(input())

while True:
    if (filas == columnas):

        print ('Ingreso de matriz A: ')
        A = agregar_datos_matriz(filas, columnas)
        A = np.array(A)
        diagonalDominante(A)
        while True:
            if (diagonalDominante(A) == True):
                print ('Ingreso de matriz B: ')
                B = agregar_datos_matriz(filas , 1)
                B = np.array(B)
                print ('Ingreso de matriz con valores iniciales: ')
                X0 = agregar_datos_matriz (filas , 1)
                X0 = np.array(X0)
                emax = float(input("Ingrese el error maximo a obtener: "))
                itermax = int(input("Ingrese el numero de iteraciones a realizar: "))
                X=gaussSeidel(A,B,X0,emax,itermax)
                # SALIDA
                X = np.transpose([X])
                print('respuesta X: ')
                print(X)
                False
            else: 
                print ('Fue al else ')
                print ('Ingreso de matriz A: ')
                A = agregar_datos_matriz(filas, columnas)
                A = np.array(A)
                diagonalDominante(A)
                True

    elif (filas != columnas):
        print ('La matriz no es cuadrada, ingrese de nuevo')
        print('Cuantas filas')
        filas = int (input())
        print ('Cuantas columnas')
        columnas = int(input())
        True



