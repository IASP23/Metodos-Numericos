import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
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
    