
x = 1.149971
y = 1.397963
h = 0.5 
def f(x , y): #aquí va la funcion a evaluar
    resx = (0.5*x-0.7*x*y)
    resy = (-0.35*x+0.35*x*y)
    print ('x = ', resx)
    print ('y =',resy)

print (f(x,y))