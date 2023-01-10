import funciones
import numpy.linalg as lin


def solucionL(A,B,n):
    x= lin.solve(A,B)
    return x


def solucionU(A,B,n):
    x= lin.solve(A,B)
    return x

def imprimeMatriz(A):
	for i in range(len(A)):
		text = " |"
		for j in range(len(A[i])):
			if(j==len(A)):
				text = text +str("%10.6f"%A[i][j])
			else:
				 text = text +str("%10.6f"%A[i][j])
		print (text+"| ")
	print ()


def metodoLU1(A,B,n):
	L = []
	for i in range(n):
		L.append( [0]*n)
	U = []
	for i in range(n):
		U.append( [0]*n)
	#pivot
	a = funciones.matrizAumentada(A,B,n)
	for j in range(n):
		a = funciones.pivot(a, j)
	A = []
	B = []
	for i in range(n):
		A.append(a[i][0:n])
		B.append(a[i][n])
	#LU1
	for j in range(0,n):
		U[j][j] = 1.0
		for i in range(j,n):
			L[i][j] = A[i][j] - funciones.suma(U,L,i,j,j)#ultima j por i
		for i in range(j+1,n):
			if L[j][j] == 0:
				return ["NULL","NULL"]
			U[j][i] = (A[j][i] - funciones.suma(U,L,j,i,j))/L[j][j]
	
	print ("\n Resolucion por Algoritmo LU1-Crout ")
	print (" -------------------------------------------------")
	print ("\n Matriz U Triangular Superior")
	imprimeMatriz(U)
	print ("\n Matriz L Triangular Inferior")
	imprimeMatriz(L)

	y = solucionL(L,B,n)	#Ly = b  "obtenemos y"
	x = solucionU(U,y,n)	#Ux = y  "obtenemos x"

	return y , x

def metodoDoolittle(A, B, n):

	U = [[0.0]*n for j in range(n)]
	L = [[float(i == j) for j in range(n)] for i in range(n)]
	
	a = funciones.matrizAumentada(A,B,n)
	for j in range(n):
		a = funciones.pivot(a, j)
	A = []
	B = []
	for i in range(n):
		A.append(a[i][0:n])
		B.append(a[i][n])

	for k in range(n):
		for i in range(k+1):
			U[i][k] = A[i][k] - sum(L[i][p]*U[p][k] for p in range(i))
		for i in range(k+1, n):
			if U[k][k] == 0:
				return L,U,["NULL","NULL"]
			L[i][k] = (A[i][k] - sum(L[i][p]*U[p][k] for p in range(k))) / float(U[k][k])
	
	print ("\n Resolucion por Algoritmo LU-Doolittle ")
	print (" -------------------------------------------------")
	print ("\n Matriz U Triangular Superior")
	imprimeMatriz(U)
	print ("\n Matriz L Triangular Inferior")
	imprimeMatriz(L)

	y = solucionL(L,B,n)	#Ly = b  "obtenemos y"
	x = solucionU(U,y,n)	#Ux = y  "obtenemos x"

	return y,x

'''
A = [[1,2,-1,3],[2,0,2,-1],[-1,1,1,-1],[3,3,-1,2]]
B= [[-8],[13],[8],[-1]]
'''

A = [[3.0 , -0.1, -0.2],[0.1, 7 ,-0.3],[0.3,-0.2, 10]]
B = [[7.85],[-19.3],[71.4]]


n = len(A)
d = metodoLU1 (A,B,n)
print (d)


