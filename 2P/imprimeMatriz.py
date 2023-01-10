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


A =[[ 2, 1,  0, 4],
	[-4,-2,  3,-7],
	[ 4, 1, -2, 8],
	[ 0,-3,-12,-1]
	]

imprimeMatriz(A)