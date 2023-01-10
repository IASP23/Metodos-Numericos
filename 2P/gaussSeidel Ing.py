# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:46:08 2021

@author: ASUS I7 10MA
"""

import numpy as np

# PROCEDIMIENTO

# Gauss-Seidel
def gaussSeidel(A,B,X0,emax,itermax):

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
        # revisa si NO converge
        if (itera>itermax):
            X=0
    return X
    # Respuesta X en columna
       

# INGRESO
A = np.array([[10. , 0, -1],
              [4,  12  , -4],
              [4, 4, 10  ]])

B = np.array([-1,8,4])

X0  = np.array([0.,0.,0.])

emax = 0.0000000000001
itermax = 100

X=gaussSeidel(A,B,X0,emax,itermax)

# SALIDA
X = np.transpose([X])
print('respuesta X: ')
print(X)

# revisa respuesta
#verifica = np.dot(A,X)
# print('verificar A.X=B: ')
# print(verifica)