import numpy as np
puntos = 2


print ('\tUniversidad de las Fuerzas Armadas ESPE-L\n')
print ('Metodos de integracion numerica')
print ('Metodo de Gauss Legendre')

def funcion(x): #aquí va la funcion a evaluar
    res =  ((2*x**2+1)*np.e**(-x**2))/x**2
    return res

b = 2 
a = 1 

if (puntos == 2):
    t1 = - 1/np.sqrt(3)
    t2 = 1/np.sqrt(3)
    lam = 1 

    x1 = (b-a)/2*t1+(a+b)/2
    x2 = (b-a)/2*t2+(a+b)/2
    fx1 = funcion(x1)
    fx2 = funcion(x2)
    print (fx1)
    print (fx2)

    integral = ((b-a)/2)*(lam*fx1+lam*fx2)
    print ('Resulta por el metodo de Gauss Legendre',integral)
elif (puntos == 3):
    t1 = -np.sqrt(6)
    t2 = 0 
    t3 = np.sqrt(6)
    lam = 5/9

    x1 = (b-a)/2*t1+(a+b)/2
    x2 = (b-a)/2*t2+(a+b)/2
    x3 = (b-a)/2*t3+(a+b)/2

    fx1 = funcion(x1)
    fx2 = funcion(x2)
    fx3 = funcion(x3)

    integral = ((b-a)/2)*(lam*fx1+lam*fx2+lam*fx3)
    print ('Resulta por el metodo de Gauss Legendre',integral)

