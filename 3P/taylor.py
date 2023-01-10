# Aproximación Polinomio de Taylor alrededor de x0
# f(x) en forma simbólica con sympy
# Burden 7Ed Capítulo 1.1 Ejemplo 3.p11,pdf21;9Ed p11.

import numpy as np
import sympy as sym


# INGRESO
x  = sym.Symbol('x')
fx = sym.cos(x) 
x0 = 0
grado = 2       # grado>0
n  = grado + 1  # Términos de polinomio

# PROCEDIMIENTO

k = 0 # contador de términos
polinomio = 0
while (k < n):
    derivada   = fx.diff(x,k)
    derivadax0 = derivada.subs(x,x0)
    divisor   = np.math.factorial(k)
    terminok  = (derivadax0/divisor)*(x-x0)**k
    polinomio = polinomio + terminok
    k = k + 1

# SALIDA
print(polinomio)