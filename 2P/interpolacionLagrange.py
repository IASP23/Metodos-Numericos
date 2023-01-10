import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def lagrange (xi , fi ):
    # Polinomio de Lagrange
    n = len(xi)
    x = sym.Symbol('x')
    polinomio = 0
    divisorL = np.zeros(n, dtype = float)
    for i in range(0,n,1):
        
        # Termino de Lagrange
        numerador = 1
        denominador = 1
        for j  in range(0,n,1):
            if (j!=i):
                numerador = numerador*(x-xi[j])
                denominador = denominador*(xi[i]-xi[j])
        terminoLi = numerador/denominador

        polinomio = polinomio + terminoLi*fi[i]
        divisorL[i] = denominador

    # simplifica el polinomio
    polisimple = polinomio.expand()

    # para evaluación numérica
    px = sym.lambdify(x,polisimple)

    # Puntos para la gráfica
    muestras = 101
    a = np.min(xi)
    b = np.max(xi)
    pxi = np.linspace(a,b,muestras)
    pfi = px(pxi)

    # SALIDA
    print('    valores de fi: ',fi)
    print('divisores en L(i): ',divisorL)
    print()
    print('Polinomio de Lagrange, expresiones')
    print(polinomio)
    print()
    print('Polinomio de Lagrange: ')
    print(polisimple)

    # Gráfica
    plt.plot(xi,fi,'o', label = 'Puntos')
    plt.plot(pxi,pfi, label = 'Polinomio')
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Interpolación Lagrange')
    plt.show()

# INTERPOLACION DE LAGRANGE MESES 

xi = np.array([2,5,6,8,10,
12,14,16,19])
fi = np.array([18022,99813,
230478,357981,469010,684453,
994048,1255909,2257085])

print ('Interpolacion de Lagrange Meses\n' , lagrange(xi,fi))

# INTERPOLACION DE LAGRANGE SEMANAS 

xi = np.array([9,18,27,36,45,54,
63,72,82])
fi = np.array([20951,113001,261598,394981,
530741,798435,1158031,1370973,1718088])

print ('Interpolacion de Lagrange Semanas\n' , lagrange(xi,fi))

# INTERPOLACION DE LAGRANGE DIAS  

xi = np.array([64,128,192,256,320,
384,448,512,577])
fi = np.array([21955,117640,272060,408195,
553646,839617,1209921,1410473,1533292
])
print ('Interpolacion de Lagrange Dias\n' , lagrange(xi,fi))
