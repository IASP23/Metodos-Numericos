def sumatoriaPrincipal (N):
    s1 = 0
    for n in range (1 ,2*N+1):
        s1+= ((-1)**n ) *( n / (n+1))
    return s1 


def literalA (N):
    s1 = 0 
    s2 = 0
    for n in range (1,N+1):
        s1+= (2*n-1)/(2*n)
        s2+= (2*n)/(2*n+1)
    return -s1+s2


def literalB (N):
    s1=0
    for n in range (1, N+1):
        s1+= (1)/(2*n*(2*n+1))
    return s1


def literalC (N):
    resultado = literalA(N)-literalA(N)
    if resultado == 0 :
        print ('Literal A y literal B son iguales')
    else:
        print ('No son iguales')
    return resultado

N = int(input('Digite un valor grande de N: '))

print ('Considerando la suma principal su resultado hasta',N,'es',sumatoriaPrincipal(N))    
print ('Se muestra que S1=',literalA(N))
print ('La sumatoria S1= ',literalB(N))
print ('Calculando las 2 expresiones es igual a: ', literalC(N))
  
