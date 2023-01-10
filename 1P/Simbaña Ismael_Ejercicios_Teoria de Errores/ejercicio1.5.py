def primeraSol (a, b, c):
    x1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
    x2 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
    return x1 , x2 

def solucionAlt (a ,b , c):
    x1p =   (-2*a*c)/(b+(b**2-4*a*c)**(1/2))
    x2p =   (-2*a*c)/(b-(b**2-4*a*c)**(1/2))
    return x1p , x2p 

print ('Cuando k=1 en x1=',primeraSol(1,1,10**-1))
print ('Cuando k=1 en x2=',primeraSol(1,1,10**-2))
print ("Cuando k=2 en d(x1)/dx=",solucionAlt(1,1,10**-1))
print ('Cuando k=2 en d(x2)/dx=',solucionAlt(1,1,10**-2))