
def polinomio1 (x):
    px=  ((x-2)**7)*(x-3)*(x-4)
    return px 

def polinomioExt (x):
    polEx = -1536 + 6272*x - 11328* x**2 + 11872*x**3
    -7952*x**4+3528*x**5-1036*x**6 + 194 *x**7 - 21*x**8 + x**9
    return(polEx)

print ('El resultado del polinomio es: ',polinomio1(1.99))
print ('El resultado del polinomio extendido es: ',polinomioExt(1.99))

