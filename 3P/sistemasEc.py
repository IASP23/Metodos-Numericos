import numpy as np
import matplotlib.pyplot as plt

# Para h = 0.1 
n = 9 
xo = 0
yo = 1
xf = 1 
yf = 1
h = (xf - xo)/(n+1)
h = 0.1
x = np.linspace(xo, xf, n+2)

xi = 0.5
b = np.zeros(n)
A = np.eye(n) * 2.2

for k in range(0, n-1):
    A[k][k+1] = (-1.1+xi*h)
    A[k+1][k] = (-0.9-xi*h)
b[0] = -(2 + h) * yo
b[n-1] = -(2 - h) * yf
y = np.linalg.inv(A).dot(b)
y = np.insert(y, 0, yo)
y = np.insert(y, n+1, yf)
print ("---------------------------------------")
print ('Valores de x: ',x)
print('Respuesta para 0.1: ',y)

plt.plot(x, y)


# Para h = 0.01 
n = 99
xo = 0
yo = 1
xf = 1 
yf = 1
h = (xf - xo)/(n+1)
h = 0.1
x = np.linspace(xo, xf, n+2)
print (x)
xi = 0.5
b = np.zeros(n)
A = np.eye(n) * 2.2

for k in range(0, n-1):
    A[k][k+1] = (-1.1+xi*h)
    A[k+1][k] = (-0.9-xi*h)
b[0] = -(2 + h) * yo
b[n-1] = -(2 - h) * yf
y = np.linalg.inv(A).dot(b)
y = np.insert(y, 0, yo)
y = np.insert(y, n+1, yf)
print ("---------------------------------------")
print ('Valores de x: ',x)
print('Respuesta para 0.001: ',y)

plt.plot(x, y)


# Para h = 0.05 
n = 199
xo = 0
yo = 1
xf = 1 
yf = 1
h = (xf - xo)/(n+1)
h = 0.1
x = np.linspace(xo, xf, n+2)
print (x)
xi = 0.5
b = np.zeros(n)
A = np.eye(n) * 2.2

for k in range(0, n-1):
    A[k][k+1] = (-1.1+xi*h)
    A[k+1][k] = (-0.9-xi*h)
b[0] = -(2 + h) * yo
b[n-1] = -(2 - h) * yf
y = np.linalg.inv(A).dot(b)
y = np.insert(y, 0, yo)
y = np.insert(y, n+1, yf)
print ("---------------------------------------")
print ('Valores de x: ',x)
print('Respuesta para 0.005: ',y)

plt.plot(x, y)
plt.show()
