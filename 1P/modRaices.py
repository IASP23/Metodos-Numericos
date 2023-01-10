def delta (a,b,c):
    d=b**2 - 4*a*c
    return d

def cant (a,b,c):
    d=delta(a,b,c)
    if d < 0:
        return 0 , d
    else:
        if d > 0:
            return 2 , d
        else:
            return 1 , d
     
def raices (a,b,c):
    d=delta(a,b,c)
    x1= (-b+(d**(0.5)))/2*a
    x2= (-b-(d**(0.5)))/2*a
    return x1,x2
