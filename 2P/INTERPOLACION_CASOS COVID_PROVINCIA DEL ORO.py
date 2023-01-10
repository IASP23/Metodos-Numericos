"""
MATERIA: METODOS NUMERICOS 8231
FECHA: 21 DE ENERO DEL 2022
TRABAJO COLABORATIVO CORRESPONDIENTE AL SEGUNDO PARCIAL
""" 

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
    
    # PROCEDIMIENTO
def interpolacionNewton (xi,fi):
    # Tabla de Diferencias Divididas Avanzadas
    titulo = ['i   ','xi  ','fi  ']
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
    np.set_printoptions(precision = 4)
    print('\nTabla Diferencia Dividida')
    print([titulo])
    print(tabla)
    print('dDividida: ')
    print(dDividida)
    print('\npolinomio: ')
    print(polinomio)
    print('\npolinomio simplificado: ' )
    print(polisimple)
    
    # Gráfica
    plt.plot(xi,fi,'o', label = 'Puntos')
    ##for i in range(0,n,1):
    ##    plt.axvline(xi[i],ls='--', color='yellow')
    plt.plot(pxi,pfi, label = 'Polinomio')
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Diferencias Divididas - Newton')
    plt.show()

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
    print('Polinomio de Lagrange, expresiones')
    print(polinomio)

    # Gráfica
    plt.plot(xi,fi,'o', label = 'Puntos')
    plt.plot(pxi,pfi, label = 'Polinomio')
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Interpolación Lagrange')
    plt.show()



print("Elija el metodo a usar para realizar la interpolacion: ")

print("1.Metodo de Newton")
print("2.Metodo de Lagrange")
print("3.Metodo de Splines cubicos")
print("4.Metodo de Minimos Cuadrados")
print("5.Salir")
    
elegir = int(input())
    
if (elegir == 1 ):
    print ('\n--------------INTERPOLACION POR EL METODO DE NEWTON-----------')
    print(" 1: INTERPOLACION POR SEMANAS\n 2: INTERPOLACION POR MESES\n 3: INTERPOLACION POR DIAS")
    m=int(input('INGRESE LA INTERPOLACION QUE DESEE OBSERVAR: '))
    if (m==1):
    #Semanas
        xi = np.array([8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 87])
        fi = np.array([839, 2496, 5162, 6939, 9584, 14091, 19971, 22353, 23646, 24218, 30477])
        print (interpolacionNewton(xi,fi))
    elif (m==2):
    #Meses
        xi = np.array([1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 21, 22])
        fi = np.array([34, 474, 1094, 3181, 5523, 7367, 10497, 14986, 20533, 22636, 23728, 23786, 25882, 34071])
        print (interpolacionNewton(xi,fi))

    elif (m==3):
    #dias
        xi = np.array([60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 673])
        fi = np.array([710, 2329, 4779, 6577, 8547, 13306, 19062, 21830, 23558, 23919, 26082,30477])  
        print (interpolacionNewton(xi,fi))
                

                
elif (elegir == 2):
    # INTERPOLACION DE LAGRANGE MESES 
    print ('\n--------------INTERPOLACION POR EL METODO DE LAGRANGE-----------')
    print(" 1: INTERPOLACION POR SEMANAS\n 2: INTERPOLACION POR MESES\n 3: INTERPOLACION POR DIAS")
    m=int(input('INGRESE LA INTERPOLACION QUE DESEE OBSERVAR: '))

    if (m == 1):
        print ('Interpolacion de Lagrange Semanas\n' )
        xi = np.array([9,18,27,36,45,54,
        63,72,82])
        fi = np.array([20951,113001,261598,394981,
        530741,798435,1158031,1370973,1718088])
        print (lagrange(xi,fi))

    elif (m == 2 ):
        print ('Interpolacion de Lagrange Meses\n')
        xi = np.array([2,5,6,8,10,
        12,14,16,19])
        fi = np.array([18022,99813,
        230478,357981,469010,684453,
        994048,1255909,2257085])
        print (lagrange(xi,fi))


    # INTERPOLACION DE LAGRANGE DIAS  
    elif (m == 3):
        print ('Interpolacion de Lagrange Dias\n' )
        #xi = np.array([64,128,192,256,320,
        #384,448,512,577])
        #fi = np.array([21955,117640,272060,408195,
        #553646,839617,1209921,1410473,1533292
        #])
        #print (lagrange(xi,fi))
        xi = np.array([2,5,6,8,10,
        12,14,16,19])
        fi = np.array([18022,99813,
        230478,357981,469010,684453,
        994048,1255909,2257085])
        print (lagrange(xi,fi))
            

elif (elegir == 3 ):
    print ('\n--------------INTERPOLACION POR EL METODO DE SPLENES-----------')
    print(" 1: INTERPOLACION POR SEMANAS\n 2: INTERPOLACION POR MESES\n 3: INTERPOLACION POR DIAS")
    m=int(input('INGRESE LA INTERPOLACION QUE DESEE OBSERVAR: '))

    if m==1:
        
        def traza3natural(xi,yi):
            n = len(xi)
            
            # Valores h
            h = np.zeros(n-1, dtype = float)
            for j in range(0,n-1,1):
                h[j] = xi[j+1] - xi[j]
            
            # Sistema de ecuaciones
            A = np.zeros(shape=(n-2,n-2), dtype = float)
            B = np.zeros(n-2, dtype = float)
            S = np.zeros(n, dtype = float)
        
            A[0,0] = 2*(h[0]+h[1])
            A[0,1] = h[1]
            B[0] = 6*((yi[2]-yi[1])/h[1] - (yi[1]-yi[0])/h[0])
        
            for i in range(1,n-3,1):
                A[i,i-1] = h[i]
                A[i,i] = 2*(h[i]+h[i+1])
                A[i,i+1] = h[i+1]
                factor21 = (yi[i+2]-yi[i+1])/h[i+1]
                factor10 = (yi[i+1]-yi[i])/h[i]
                B[i] = 6*(factor21 - factor10)
                
            A[n-3,n-4] = h[n-3]
            A[n-3,n-3] = 2*(h[n-3]+h[n-2])
            factor12 = (yi[n-1]-yi[n-2])/h[n-2]
            factor23 = (yi[n-2]-yi[n-3])/h[n-3]
            B[n-3] = 6*(factor12 - factor23)
            
            # Resolver sistema de ecuaciones S
            r = np.linalg.solve(A,B)
            for j in range(1,n-1,1):
                S[j] = r[j-1]
            S[0] = 0
            S[n-1] = 0
            
            # Coeficientes
            a = np.zeros(n-1, dtype = float)
            b = np.zeros(n-1, dtype = float)
            c = np.zeros(n-1, dtype = float)
            d = np.zeros(n-1, dtype = float)
            for j in range(0,n-1,1):
                a[j] = (S[j+1]-S[j])/(6*h[j])
                b[j] = S[j]/2
                factor10 = (yi[j+1]-yi[j])/h[j]
                c[j] = factor10 - (2*h[j]*S[j]+h[j]*S[j+1])/6
                d[j] = yi[j]
            
            # Polinomio trazador
            x = sym.Symbol('x')
            px_tabla = []
            for j in range(0,n-1,1):
        
                pxtramo = a[j]*(x-xi[j])**3 + b[j]*(x-xi[j])**2
                pxtramo = pxtramo + c[j]*(x-xi[j])+ d[j]
                
                pxtramo = pxtramo.expand()
                px_tabla.append(pxtramo)
            
            return(px_tabla)
        
        # PROGRAMA -----------------------
        # INGRESO , Datos de prueba
        xi = np.array([504,1680,2856,4032,5208,6384,7560,8232,9912,11088,12264,13440,14616,15792,16968,18144,19320,20496,21672,22848,24024,25200,26376,27552,28728,29904,31080,32256,33432,34608,35784,36960,38136,39312,40488,41664,42840,44016,45192,46368,47544,48720,49896,51072,52248,53424,54600,55776,56952,58128,59304,60480,61656,64008,65184,66360,67536,68712,69888,71064,72240,73416,74592,75768,76944,78120,79296,80472,81648,82824,84000,85176,86352,87528,88704,89880,91056,92232,93408,94584,95760])
        fi = np.array([13,129,340,731,1220,2383,3960,4250,6252,7180,7900,9105,10574,12430,13896,15177,16540,18435,20290,22759,24872,27094,28795,30600,32667,35169,36776,37746,39552,40975,42181,44069,45276,45946,47908,49460,51309,52598,53953,55679,57246,59038,62152,66157,69649,73019,76237,80691,84116,87847,92133,96275,99688,103432,108565,113709,118895,124434,129368,134754,138293,141195,143388,145044,146783,148346,150263,152222,153992,155639,157851,158452,161419,162640,163647,164387,164925,165231,165463,165722,166144])
        #print('Ingrese el valor a interpolar a x')
        #p=float(input("ingrese valor :"))
        
        muestras = 10 # entre cada par de puntos
        
        # PROCEDIMIENTO
        # Tabla de polinomios por tramos
        n = len(xi)
        px_tabla = traza3natural(xi,fi)
        
        # SALIDA
        print('Polinomios por tramos: ')
        for tramo in range(1,n,1):
            print(' x = ['+str(xi[tramo-1])
                +','+str(xi[tramo])+']')
            print(str(px_tabla[tramo-1]))
            
        
        #Evaluar
        
        #val=0.193181818181818*p**3 - 1.73863636363636*p**2 + 2.94318181818182*p + 0.602272727272727
        #print("El valor interpolado para  x=2 es ",val)
            
            
        # GRAFICA
        # Puntos para graficar cada tramo
        xtraza = np.array([])
        ytraza = np.array([])
        tramo = 1
        while not(tramo>=n):
            a = xi[tramo-1]
            b = xi[tramo]
            xtramo = np.linspace(a,b,muestras)
            
            # evalua polinomio del tramo
            pxtramo = px_tabla[tramo-1]
            pxt = sym.lambdify('x',pxtramo)
            ytramo = pxt(xtramo)
        
            # vectores de trazador en x,y
            xtraza = np.concatenate((xtraza,xtramo))
            ytraza = np.concatenate((ytraza,ytramo))
            tramo = tramo + 1
        
        # Gráfica
        plt.plot(xi,fi,'ro', label='puntos')
        plt.plot(xtraza,ytraza, label='trazador'
                , color='blue')
        plt.title('Trazadores Cúbicos Naturales(Semanas)')
        plt.xlabel('xi')
        plt.ylabel('px(xi)')
        plt.legend()
        plt.show()
        
    elif m==2:
        
        def traza3natural(xi,yi):
            n = len(xi)
            
            # Valores h
            h = np.zeros(n-1, dtype = float)
            for j in range(0,n-1,1):
                h[j] = xi[j+1] - xi[j]
            
            # Sistema de ecuaciones
            A = np.zeros(shape=(n-2,n-2), dtype = float)
            B = np.zeros(n-2, dtype = float)
            S = np.zeros(n, dtype = float)
        
            A[0,0] = 2*(h[0]+h[1])
            A[0,1] = h[1]
            B[0] = 6*((yi[2]-yi[1])/h[1] - (yi[1]-yi[0])/h[0])
        
            for i in range(1,n-3,1):
                A[i,i-1] = h[i]
                A[i,i] = 2*(h[i]+h[i+1])
                A[i,i+1] = h[i+1]
                factor21 = (yi[i+2]-yi[i+1])/h[i+1]
                factor10 = (yi[i+1]-yi[i])/h[i]
                B[i] = 6*(factor21 - factor10)
                
            A[n-3,n-4] = h[n-3]
            A[n-3,n-3] = 2*(h[n-3]+h[n-2])
            factor12 = (yi[n-1]-yi[n-2])/h[n-2]
            factor23 = (yi[n-2]-yi[n-3])/h[n-3]
            B[n-3] = 6*(factor12 - factor23)
            
            # Resolver sistema de ecuaciones S
            r = np.linalg.solve(A,B)
            for j in range(1,n-1,1):
                S[j] = r[j-1]
            S[0] = 0
            S[n-1] = 0
            
            # Coeficientes
            a = np.zeros(n-1, dtype = float)
            b = np.zeros(n-1, dtype = float)
            c = np.zeros(n-1, dtype = float)
            d = np.zeros(n-1, dtype = float)
            for j in range(0,n-1,1):
                a[j] = (S[j+1]-S[j])/(6*h[j])
                b[j] = S[j]/2
                factor10 = (yi[j+1]-yi[j])/h[j]
                c[j] = factor10 - (2*h[j]*S[j]+h[j]*S[j+1])/6
                d[j] = yi[j]
            
            # Polinomio trazador
            x = sym.Symbol('x')
            px_tabla = []
            for j in range(0,n-1,1):
        
                pxtramo = a[j]*(x-xi[j])**3 + b[j]*(x-xi[j])**2
                pxtramo = pxtramo + c[j]*(x-xi[j])+ d[j]
                
                pxtramo = pxtramo.expand()
                px_tabla.append(pxtramo)
            
            return(px_tabla)
        
        # PROGRAMA -----------------------
        # INGRESO , Datos de prueba
        xi = np.array([2880,19824,42120,63720,88536,111600,129960,156984,173880,202368,225432,223440,269328,282600,314712,326520,360096,383160,392760])
        fi = np.array([206,5734,25507,47553,78783,118934,151245,186103,205785,242587,289941,322596,429574,501830,609658,631549,687612,719121,708585])
        #print('Ingrese el valor a interpolar a x')
        #p=float(input("ingrese valor :"))
        
        muestras = 10 # entre cada par de puntos
        
        # PROCEDIMIENTO
        # Tabla de polinomios por tramos
        n = len(xi)
        px_tabla = traza3natural(xi,fi)
        
        # SALIDA
        print('Polinomios por tramos: ')
        for tramo in range(1,n,1):
            print(' x = ['+str(xi[tramo-1])
                +','+str(xi[tramo])+']')
            print(str(px_tabla[tramo-1]))
            
        
        #Evaluar
        
        #val=0.193181818181818*p**3 - 1.73863636363636*p**2 + 2.94318181818182*p + 0.602272727272727
        #print("El valor interpolado para  x=2 es ",val)
            
            
        # GRAFICA
        # Puntos para graficar cada tramo
        xtraza = np.array([])
        ytraza = np.array([])
        tramo = 1
        while not(tramo>=n):
            a = xi[tramo-1]
            b = xi[tramo]
            xtramo = np.linspace(a,b,muestras)
            
            # evalua polinomio del tramo
            pxtramo = px_tabla[tramo-1]
            pxt = sym.lambdify('x',pxtramo)
            ytramo = pxt(xtramo)
        
            # vectores de trazador en x,y
            xtraza = np.concatenate((xtraza,xtramo))
            ytraza = np.concatenate((ytraza,ytramo))
            tramo = tramo + 1
        
        # Gráfica
        plt.plot(xi,fi,'ro', label='puntos')
        plt.plot(xtraza,ytraza, label='trazador'
                , color='blue')
        plt.title('Trazadores Cúbicos Naturales(Meses)')
        plt.xlabel('xi')
        plt.ylabel('px(xi)')
        plt.legend()
        plt.show()
        
    elif m==3:
        def traza3natural(xi,yi):
            n = len(xi)
            
            # Valores h
            h = np.zeros(n-1, dtype = float)
            for j in range(0,n-1,1):
                h[j] = xi[j+1] - xi[j]
            
            # Sistema de ecuaciones
            A = np.zeros(shape=(n-2,n-2), dtype = float)
            B = np.zeros(n-2, dtype = float)
            S = np.zeros(n, dtype = float)
        
            A[0,0] = 2*(h[0]+h[1])
            A[0,1] = h[1]
            B[0] = 6*((yi[2]-yi[1])/h[1] - (yi[1]-yi[0])/h[0])
        
            for i in range(1,n-3,1):
                A[i,i-1] = h[i]
                A[i,i] = 2*(h[i]+h[i+1])
                A[i,i+1] = h[i+1]
                factor21 = (yi[i+2]-yi[i+1])/h[i+1]
                factor10 = (yi[i+1]-yi[i])/h[i]
                B[i] = 6*(factor21 - factor10)
                
            A[n-3,n-4] = h[n-3]
            A[n-3,n-3] = 2*(h[n-3]+h[n-2])
            factor12 = (yi[n-1]-yi[n-2])/h[n-2]
            factor23 = (yi[n-2]-yi[n-3])/h[n-3]
            B[n-3] = 6*(factor12 - factor23)
            
            # Resolver sistema de ecuaciones S
            r = np.linalg.solve(A,B)
            for j in range(1,n-1,1):
                S[j] = r[j-1]
            S[0] = 0
            S[n-1] = 0
            
            # Coeficientes
            a = np.zeros(n-1, dtype = float)
            b = np.zeros(n-1, dtype = float)
            c = np.zeros(n-1, dtype = float)
            d = np.zeros(n-1, dtype = float)
            for j in range(0,n-1,1):
                a[j] = (S[j+1]-S[j])/(6*h[j])
                b[j] = S[j]/2
                factor10 = (yi[j+1]-yi[j])/h[j]
                c[j] = factor10 - (2*h[j]*S[j]+h[j]*S[j+1])/6
                d[j] = yi[j]
            
            # Polinomio trazador
            x = sym.Symbol('x')
            px_tabla = []
            for j in range(0,n-1,1):
        
                pxtramo = a[j]*(x-xi[j])**3 + b[j]*(x-xi[j])**2
                pxtramo = pxtramo + c[j]*(x-xi[j])+ d[j]
                
                pxtramo = pxtramo.expand()
                px_tabla.append(pxtramo)
            
            return(px_tabla)
        
        # PROGRAMA -----------------------
        # INGRESO , Datos de prueba
        xi = np.array([24,48,72,96,120,144,168,192,216,240,264,288,312,336,360,384,408,432,456,480,504,528,552,576,600,624,648,672,696,720,744,768,792,816,840,864,888,912,936,960,984,1008,1032,1056,1080,1104,1128,1152,1176,1200,1224,1248,1272,1296,1320,1344,1368,1392,1416,1440,1464,1488,1512,1536,1560,1584,1608,1632,1656,1680,1704,1728,1752,1776,1800,1824,1848,1872,1896,1920,1944,1968,1992,2016,2040,2064,2088,2112,2136,2160,2184,2208,2232,2256,2280,2304,2328,2352,2376,2400,2424,2448,2472,2496,2520,2544,2568,2592,2616,2640,2664,2688,2712,2736,2760,2784,2808,2832,2856,2880,2904,2928,2952,2976,3000,3024,3048,3072,3096])
        fi = np.array([1,1,1,2,2,6,9,14,17,20,21,23,25,30,34,52,56,56,56,56,58,58,82,97,137,149,150,160,166,183,193,207,247,257,266,276,289,300,477,327,448,457,474,559,575,624,643,628,673,652,658,672,664,707,710,716,839,907,920,935,959,976,994,1004,1017,1025,1039,1050,1051,1062,1066,1088,1094,1167,1210,1213,1223,1278,1305,1309,1320,1323,1347,1380,1442,1489,1514,1574,1580,1595,1657,1743,1759,1790,1803,1817,1861,1882,1944,1976,2013,2017,2022,2042,2073,2135,2156,2173,2189,2192,2259,2278,2296,2329,2354,2406,2432,2445,2496,2580,2617,2626,2632,2739,2745,2758,2764,2879,2904])
        #print('Ingrese el valor a interpolar a x')
        #p=float(input("ingrese valor :"))
        
        muestras = 10 # entre cada par de puntos
        
        # PROCEDIMIENTO
        # Tabla de polinomios por tramos
        n = len(xi)
        px_tabla = traza3natural(xi,fi)
        
        # SALIDA
        print('Polinomios por tramos: ')
        for tramo in range(1,n,1):
            print(' x = ['+str(xi[tramo-1])
                +','+str(xi[tramo])+']')
            print(str(px_tabla[tramo-1]))
            
        
        #Evaluar
        
        #val=0.193181818181818*p**3 - 1.73863636363636*p**2 + 2.94318181818182*p + 0.602272727272727
        #print("El valor interpolado para  x=2 es ",val)
            
            
        # GRAFICA
        # Puntos para graficar cada tramo
        xtraza = np.array([])
        ytraza = np.array([])
        tramo = 1
        while not(tramo>=n):
            a = xi[tramo-1]
            b = xi[tramo]
            xtramo = np.linspace(a,b,muestras)
            
            # evalua polinomio del tramo
            pxtramo = px_tabla[tramo-1]
            pxt = sym.lambdify('x',pxtramo)
            ytramo = pxt(xtramo)
        
            # vectores de trazador en x,y
            xtraza = np.concatenate((xtraza,xtramo))
            ytraza = np.concatenate((ytraza,ytramo))
            tramo = tramo + 1
        
        # Gráfica
        plt.plot(xi,fi,'ro', label='puntos')
        plt.plot(xtraza,ytraza, label='trazador'
                , color='blue')
        plt.title('Trazadores Cúbicos Naturales(DIAS)')
        plt.xlabel('xi')
        plt.ylabel('px(xi)')
        plt.legend()
        plt.show()

elif elegir ==4 :
    x= np.array([24,48,72,96,120,144,168,192,216,240,264,288,312,336,360,384,408,
                432,456,480,504,528,552,576,600,624,648,672,696,720,744,768,792,
                816,840,864,888,912,936,960,984,1008,1032,1056,1080,1104,1128,1152,
                1176,1200,1224,1248,1272,1296,1320,1344,1368,1392,1416,1440,1464,
                1488,1512,1536,1560,1584,1608,1632,1656,1680,1704,1728,1752,1776,
                1800,1824,1848,1872,1896,1920,1944,1968,1992,2016,2040,2064,2088,
                2112,2136,2160,2184,2208,2232,2256,2280,2304,2328,2352,2376,2400,
                2424,2448,2472,2496,2520,2544,2568,2592,2616,2640,2664,2688,2712,
                2736,2760,2784,2808,2832,2856,2880,2904,2928,2952,2976,3000,3024,
                3048,3072,3096,3120,3144,3168,3192,3216,3240,3264,3288,3312,3336,
                3360,3384,3408,3432,3456,3480,3504,3528,3552,3576,3600,3624,3648,
                3672,3696,3720,3744,3768,3792,3816,3840,3864,3888,3912,3936,3960,
                3984,4008,4032,4056,4080,4104,4128,4152,4176,4200,4224,4248,4272,
                4296,4320,4344,4368,4392,4416,4440,4464,4488,4512,4536,4560,4584,
                4608,4632,4656,4680,4704,4728,4752,4776,4800,4824,4848,4872,4896,
                4920,4944,4968,4992,5016,5040,5064,5088,5112,5136,5160,5184,5208,
                5232,5256,5280,5304,5328,5352,5376,5400,5424,5448,5472,5496,5520,
                5544,5568,5592,5616,5640,5664,5688,5712,5736,5760,5784,5808,5832,
                5856,5880,5904,5928,5952,5976,6000,6024,6048,6072,6096,6120,6144,
                6168,6192,6216,6240,6264,6288,6312,6336,6360,6384,6408,6432,6456,
                6480,6504,6528,6552,6576,6600,6624,6648,6672,6696,6720,6744,6768,
                6792,6816,6840,6864,6888,6912,6936,6960,6984,7008,7032,7056,7080,
                7104,7128,7152,7176,7200,7224,7248,7272,7296,7320,7344,7368,7392,
                7416,7440,7464,7488,7512,7536,7560,7584,7608,7632,7656,7680,7704,
                7728,7752,7776,7800,7824,7848,7872,7896,7920,7944,7968,7992,8016,
                8040,8064,8088,8112,8136,8160,8184,8208,8232,8256,8280,8304,8328,
                8352,8376,8400,8424,8448,8472,8496,8520,8544,8568,8592,8616,8640,
                8664,8688,8712,8736,8760,8784,8808,8832,8856,8880,8904,8928,8952,
                8976,9000,9024,9048,9072,9096,9120,9144,9168,9192,9216,9240,9264,
                9288,9312,9336,9360,9384,9408,9432,9456,9480,9504,9528,9552,9576,
                9600,9624,9648,9672,9696,9720,9744,9768,9792,9816,9840,9864,9888,
                9912,9936,9960,9984,10008,10032,10056,10080,10104,10128,10152,10176,
                10200,10224,10248,10272,10296,10320,10344,10368,10392,10416,10440,
                10464,10488,10512,10536,10560,10584,10608,10632,10656,10680,10704,
                10728,10752,10776,10800,10824,10848,10872,10896,10920,10944,10968,
                10992,11016,11040,11064,11088,11112,11136,11160,11184,11208,11232,
                11256,11280,11304,11328,11352,11376,11400,11424,11448,11472,11496,
                11520,11544,11568,11592,11616,11640,11664,11688,11712,11736,11760,
                11784,11808,11832,11856,11880,11904,11928,11952,11976,12000,12024,
                12048,12072,12096,12120,12144,12168,12192,12216,12240,12264,12288,
                12312,12336,12360,12384,12408,12432,12456,12480,12504,12528,12552,
                12576,12600,12624,12648,12672,12696,12720,12744,12768,12792,12816,
                12840,12864,12888,12912,12936,12960,12984,13008,13032,13056,13080,
                13104,13128,13152,13176,13200,13224,13248,13272,13296,13320,13344,
                13368,13392,13416,13440,13464,13488,13512,13536,13560,13584,13608,
                13632,13656,13680,13704,13728,13752,13776,13800,13824,13848])
    y = np.array([1,1,1,2,2,6,9,14,17,20,21,23,25,30,34,52,56,56,56,56,58,58,82,97,137
                ,149,150,160,166,183,193,207,247,257,266,276,289,300,477,327,448,
                457,474,559,575,624,643,628,673,652,658,672,664,707,710,716,839,907,
                920,935,959,976,994,1004,1017,1025,1039,1050,1051,1062,1066,1088,
                1094,1167,1210,1213,1223,1278,1305,1309,1320,1323,1347,1380,1442,
                1489,1514,1574,1580,1595,1657,1743,1759,1790,1803,1817,1861,1882,
                1944,1976,2013,2017,2022,2042,2073,2135,2156,2173,2189,2192,2259,
                2278,2296,2329,2354,2406,2432,2445,2496,2580,2617,2626,2632,2739,
                2745,2758,2764,2879,2904,2922,3001,3062,3118,3181,3233,3248,3291,
                3342,3346,3357,3414,3492,3588,3634,3666,3721,3755,3821,3845,3870,
                3877,3958,3968,3987,4041,4056,4103,4159,4215,4234,4277,4330,4345,
                4376,4385,4423,4464,4510,4560,4629,4707,4727,4755,4779,4877,4951,
                4984,5053,5082,5095,5127,5162,5206,5243,5277,5280,5295,5313,5334,
                5352,5371,5382,5384,5400,5523,5600,5619,5635,5640,5654,5664,5740,
                5797,5828,5832,5833,5844,5905,5936,5964,6008,6009,6028,6038,6040,
                6094,6160,6253,6293,6295,6310,6350,6408,6433,6441,6452,6477,6483,
                6493,6497,6497,6497,6524,6577,6577,6605,6669,6706,6785,6842,6870,
                6872,6894,6939,6975,6993,7046,7073,7104,7113,7156,7202,7279,7311,
                7362,7367,7390,7398,7418,7462,7502,7541,7549,7560,7566,7620,7652,
                7691,7730,7732,7748,7780,7819,7901,7938,7985,7998,7998,8040,8084,
                8147,8153,8153,8199,8213,8297,8323,8343,8435,8438,8452,8500,8547,
                8613,8680,8796,8872,8999,9048,9144,9235,9321,9425,9466,9478,9584,
                9648,9768,9830,9872,10011,10023,10067,10078,10162,10187,10422,10497,
                10548,10570,10633,10647,10746,10811,10979,11004,11021,11029,11199,
                11325,11475,11600,11657,11716,11719,11772,11833,11910,12068,12086,
                12177,12270,12299,12382,12495,12625,12633,12648,12765,12806,12964,
                13012,13301,13306,13325,13419,13490,13577,13712,13825,13863,13872,
                13936,13989,14091,14209,14298,14326,14332,14443,14508,14621,14654,
                14855,14870,14938,14986,15159,15278,15288,15591,15707,15732,15810,
                15853,16002,16087,16342,16344,16513,16568,16724,16730,16911,17037,
                17037,17136,17320,17354,17610,17746,17786,17925,17969,18044,18107,
                18120,18352,18507,18668,18802,18812,18929,19062,19193,19283,19341,
                19435,19511,19532,19592,19776,19789,19842,19862,19900,19971,20052,
                20137,20223,20246,20268,20298,20374,20398,20442,20528,20533,20536,
                20577,20589,20639,20703,20743,20775,20795,20800,20841,20880,20957,
                21004,21010,21019,21072,21091,21138,21174,21178,21223,21242,21300,
                21307,21384,21430,21456,21508,21584,21594,21648,21668,21734,21734,
                21768,21830,21840,21883,21968,22002,22027,22027,22029,22056,22077,
                22158,22180,22235,22254,22353,22382,22429,22517,22517,22517,22599,
                22636,22636,22636,22636,22636,22636,22636,22636,22636,22970,23007,
                23032,23086,23097,23102,23125,23158,23189,23225,23248,23250,23274,
                23296,23322,23349,23382,23387,23389,23402,23416,23434,23456,23485,
                23494,23495,23507,23516,23526,23542,23558,23569,23570,23573,23587,
                23589,23591,23607,23607,23608,23613,23616,23619,23634,23638,23639,
                23640,23646,23647,23647,23657,23675,23675,23676,23693,23699,23728,
                23728,23728,23728,23742,23742,23748,23758,23763,23764,23764,23767,
                23771,23771,23775,23777,23784,23786])

    m = (len(x) * np.sum(x*y) - np.sum(x) * np.sum(y)) / (len(x)*np.sum(x*x) - np.sum(x) ** 2)
    b = (np.sum(y) - m *np.sum(x)) / len(x)
    print('El valor de a=',m)
    print('El valor de b=',b)
    print('Ecuacion =',m,'x +',b)
    print('\n\n')

    def predict(x):
        return m*x - b
    vec = np.arange(-10000000)
    plt.scatter(x,y, color='red')
    plt.plot(vec,predict(vec))
    plt.xlabel("Horas Días")
    plt.ylabel("Contagios por Día")
    plt.title('Minimos Cuadrados')
    plt.show()

    x_2 = np.array([504,1680,2856,4032,5208,6384,7560,8232,9912,11088,12264,13440,14616,
                    15792,16968,18144,19320,20496,21672,22848,24024,25200,26376,27552,
                    28728,29904,31080,32256,33432,34608,35784,36960,38136,39312,40488,
                    41664,42840,44016,45192,46368,47544,48720,49896,51072,52248,53424,
                    54600,55776,56952,58128,59304,60480,61656,62832,64008,65184,66360,
                    67536,68712,69888,71064,72240,73416,74592,75768,76944,78120,79296,
                    80472,81648,82824,84000,85176,86352,87528,88704,89880,91056,92232,
                    93408,94584,95760,55248])
    y_2 = np.array([13,129,340,731,1220,2383,3960,4250,6252,7180,7900,9105,10574,12430,
                    13896,15177,16540,18435,20290,22759,24872,27094,28795,30600,32667,
                    35169,36776,37746,39552,40975,42181,44069,45276,45946,47908,49460,
                    51309,52598,53953,55679,57246,59038,62152,66157,69649,73019,76237,
                    80691,84116,87847,92133,96275,99688,103432,108565,113709,118895,
                    124434,129368,134754,138293,141195,143388,145044,146783,148346,
                    150263,152222,153992,155639,157851,158452,161419,162640,163647,
                    164387,164925,165231,165463,165722,166144,166358,95122])
    n = (len(x_2) * np.sum(x_2*y_2) - np.sum(x_2) * np.sum(y_2)) / (len(x_2)*np.sum(x_2*x_2) - np.sum(x_2) ** 2)
    c = (np.sum(y_2) - n *np.sum(x_2)) / len(x_2)
    print('El valor de a=',n)
    print('El valor de b=',c)
    print('Ecuacion =',n,'x +',c)
    print('\n\n')


    def predict2(x_2):
        return n*x_2 - c
    plt.scatter(x_2,y_2, color='blue')
    plt.plot(vec,predict2(vec))
    plt.xlabel("Horas Semanas")
    plt.ylabel("Contagios por Semanas")
    plt.title('Minimos Cuadrados')
    plt.show()


    x_3 = np.array([2880,19824,42120,63720,88536,111600,129960,156984,173880,202368,
                    225432,223440,269328,282600,314712,326520,360096,383160,392760,232152])
    y_3 = np.array([206,5734,25507,47553,78783,118934,151245,186103,205785,242587,
                    289941,322596,429574,501830,609658,631549,687612,719121,708585,403896])
    o = (len(x_3) * np.sum(x_3*y_3) - np.sum(x_3) * np.sum(y_3)) / (len(x_3)*np.sum(x_3*x_3) - np.sum(x_3) ** 2)
    d = (np.sum(y_3) - o *np.sum(x_3)) / len(x_3)
    print('El valor de a=',o)
    print('El valor de b=',d)
    print('Ecuacion =',o,'x +',d)

    def predict3(x_3):
        return o*x_3 - d
    plt.scatter(x_3,y_3, color='green')
    plt.plot(vec,predict3(vec))
    plt.xlabel("Horas Meses")
    plt.ylabel("Contagios por Meses")
    plt.title('Minimos Cuadrados')
    plt.show()