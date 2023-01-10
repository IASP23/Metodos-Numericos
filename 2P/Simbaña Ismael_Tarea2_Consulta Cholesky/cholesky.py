import math
import numpy.linalg as lin
from numpy import array

def transMatriz(M,n):
	return [[ M[i][j] for i in range(n)] for j in range(n)] 
	return M
    

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
				text = text +str("%8.3f"%A[i][j])
			else:
				 text = text +str("%8.3f"%A[i][j])
		print (text+"| ")
	print ()


def metodoCholesky(A,B, n):
	#creamos matriz nula G
	G = [[0.0]*n]*n
	#creamos matriz nula Gt
	for i in range(n):
		suma = A[i][i]
		for k in range(i):
			suma = suma - A[k][i]**2
		if suma < 0: #no es definida positiva
			return ["NULL","NULL"]
		A[i][i] = math.sqrt(suma)
		for j in range(i+1, n):
			suma = A[i][j]
			for k in range(i):
				suma = suma - A[k][i]*A[k][j]
			A[i][j] = suma / A[i][i]

	for j in range(n):
		for i in range(n):
			if(i > j):
				A[i][j] = 0.0

	G = A
	Gt = transMatriz(G,n)

	print ("\n Resolucion por Algoritmo Cholesky ")
	print (" -------------------------------------------------")
	print ("\n Matriz G Triangular Superior")
	imprimeMatriz(G)
	print ("\n Matriz Gt Triangular Inferior")
	imprimeMatriz(Gt)

	y = solucionL(Gt,B,n)	#Ly = b  "obtenemos y"
	x = solucionU(G,y,n)	#Ux = y  "obtenemos x"

	return x


print("\n\t\t\tUNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE-L\n")
print('Metodo de Cholesky')

A =[[4,-1,0,2], 
[-1, 4, -1 , 0],
[0, -1, 4 , 1],
[2, 0, 1 , 3]]

B = [[6],[3],[16],[12]]
print ('Matriz: ')
imprimeMatriz(A)
print ('B: ')
imprimeMatriz(B)

n= len(A)

print (n)

print ('Los valores para resolver el sistema son', metodoCholesky (A,B,  n), ' respectivamente')
