import numpy as np 

ec1 = np.array([[0.780 , 0.563], [0.457 , 0.330]])
igualado = np.array ([0.217, 0.127])
x = np.linalg.solve(ec1 , igualado)

print ('Valor de x: ', round(x[0], 2), 'Valor de y: ', round(x[1],1) )
