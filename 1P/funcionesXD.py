
import math  as ra
def delta (a,b,c):
    discriminante = (b**2)-(4*a*c)
    return discriminante

D = delta(1,4,7)
F = delta(1,2,3)
print('El valor del discriminante D es=' , D)
print('El valor del discriminante F es=' , F)

def cant (a,b,c):
    d=delta(a,b,c)
    if d < 0:
        return 0 
    else:
        if d > 0:
            return 2 
        else:
            return 1

Dcc = cant(1,4,4)
print('el numero de raices reales es ' , Dcc)

def raices (a, b, c):
    x1 =(-b + ra.sqrt(delta(a,b,c)))/2*a
    x2=(-b - ra.sqrt(delta(a,b,c)))/2*a
    return x1 , x2

valorRaiz = raices(1,4,4)
print('La raiz es ' ,valorRaiz)

