import math

print('------------------------------------------------------')
print('\tUniversidad de las Fuerzas Armadas ESPE-L')
print('------------------------------------------------------')
print ('\nMetodo de la regla falsa\n')
ecuacion = input('Ingrese funcion: ')
xi = float(input("xi: "))
xs = float(input("xs: "))

itmax=100
tol=1.e-5
xr=100
error=100
it=0
while error>tol and it<itmax: 

	libres=dict(x=xi) #evalua en a
	funcs = vars(math)
	fa=eval(ecuacion, funcs,libres)

	libres=dict(x=xs) #evalua en b
	funcs = vars(math)
	fb = eval(ecuacion, funcs,libres)
	
	vxr=xr
	xr=xs-((fb*(xs-xi))/(fb-fa))

	libres=dict(x=xr) #evalua en xr
	funcs = vars(math)
	fxr=eval(ecuacion, funcs,libres)	

	n_x=fa*fxr

	error=abs(((xr-vxr)/xr)*100)
		
	if n_x>0:
		xi=xr
	if n_x<0:
		xs=xr

	it +=1

print("Imagenes:\nf(xi)= ",fa)
print("f(xs)= ",fb)
print("Raiz : xr= ",xr)
print("Error: ",error)