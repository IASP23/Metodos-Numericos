
def sumatoria1 (N):
    s1 = 0
    for n in range (1 , N+1):
        s1 += 1/n 
    return s1

def sumatoria2 (N):
    s1= 0 
    for n in range (N , 0 , -1):
        s1 += 1/n 
    return s1

N = int(input('Dijite un valor grande de N: '))

print ('Considerando un valor grande de N su resultado es:',sumatoria1(N))
print ('Considerando un valor grande de N su resultado es:',sumatoria2(N))