import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO
xi = [2 , 6, 7 , 12] 
fi = [4 , 4 , 6 , 7]

xi = np.array(xi)
B = np.array(fi)
n = len(xi)

D = np.zeros(shape=(n,n),dtype =float)
for i in range(0,n,1):
    for j in range(0,n,1):
        potencia = (n-1)-j # Derecha a izquierda
        D[i,j] = xi[i]**potencia

coeficiente = np.linalg.solve(D,B)


x = sym.Symbol('x')
polinomio = 0
for i in range(0,n,1):
    potencia = (n-1)-i  
    termino = coeficiente[i]*(x**potencia)
    polinomio = polinomio + termino

px = sym.lambdify(x,polinomio)

# Para graficar el polinomio en [a,b]
a = np.min(xi)
b = np.max(xi)
xin = np.linspace(a,b)
yin = px(xin)
    
# SALIDA
print("\t\t\tUNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE-L\n")
print ('Interpolacion Cubica con gráfica\n')
print('Ejercicio 2.37')

print('Polinomio de interpolación: ')
print(polinomio)
print('\n formato pprint')

# Grafica
plt.plot(xi,fi,'o', label='[xi,fi]')
plt.plot(xin,yin, label='p(x)')
plt.xlabel('xi')
plt.ylabel('fi')
plt.legend()
plt.title(polinomio)
plt.show()