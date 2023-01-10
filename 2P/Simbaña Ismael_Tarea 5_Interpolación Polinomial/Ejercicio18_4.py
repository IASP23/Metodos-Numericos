import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def interNewton(xi , fi):
    # Tabla de Diferencias Divididas Avanzadas
    titulo = ['i   ','xi  ','fi']
    n = len(xi)
    ki = np.arange(0,n,1)
    tabla = np.concatenate(([ki],[xi],[fi]),axis=0)
    tabla = np.transpose(tabla)

    # diferencias divididas vacia
    dfinita = np.zeros(shape=(n,n),dtype=float)
    tabla = np.concatenate((tabla,dfinita), axis=1)

    # Calcula tabla, inicia en columna 3
    [n,m] = np.shape(tabla)
    diagonal = n-1
    j = 3

    while (j < m):
        # Añade título para cada columna
        titulo.append('F['+str(j-2)+']')

        # cada fila de columna
        i = 0
        paso = j-2 # inicia en 1
        while (i < diagonal):
            denominador = (xi[i+paso]-xi[i])
            numerador = tabla[i+1,j-1]-tabla[i,j-1]
            tabla[i,j] = numerador/denominador
            i = i+1
        diagonal = diagonal - 1
        j = j+1

    # POLINOMIO con diferencias Divididas
    # caso: puntos equidistantes en eje x
    dDividida = tabla[0,3:]
    n = len(dfinita)

    # expresión del polinomio con Sympy
    x = sym.Symbol('x')
    polinomio = fi[0]
    for j in range(1,n,1):
        factor = dDividida[j-1]
        termino = 1
        for k in range(0,j,1):
            termino = termino*(x-xi[k])
        polinomio = polinomio + termino*factor

    # simplifica multiplicando entre (x-xi)
    polisimple = polinomio.expand()

    # polinomio para evaluacion numérica
    px = sym.lambdify(x,polisimple)

    # Puntos para la gráfica
    muestras = 101
    a = np.min(xi)
    b = np.max(xi)
    pxi = np.linspace(a,b,muestras)
    pfi = px(pxi)
    # SALIDA
    print ('Interpolacion de Newton\n')
    np.set_printoptions(precision = 4)
    print('Tabla Diferencia Dividida')
    print([titulo])
    print(tabla)
    print('polinomio: ')
    print(polinomio)
    print('polinomio simplificado: ' )
    print(polisimple)
    return ('----------------------------------------')

# INGRESO , Datos de prueba

print("\t\t\tUNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE-L\n")

print ('Polinomio de grado 1:\n')
xi = np.array([1.6, 4.5])
fi = np.array([2 , 2 ])
print(interNewton(xi, fi))

print ('Polinomio de grado 2:\n')
xi = np.array([1.6, 3.2, 4.5])
fi = np.array([2 ,1.5,  2 ])
print(interNewton(xi, fi))

print ('Polinomio de grado 3:\n')
xi = np.array([1.6 ,2 , 3.2 , 4.5])
fi = np.array([2 , 8 , 15 , 2 ])
print(interNewton(xi, fi))

