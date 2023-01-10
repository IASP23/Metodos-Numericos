numero = int(input('Escriba un número: '))
if  numero % 2 == 0 and numero % 4 != 0:
    print(numero,'es múltiplo de dos')
elif numero % 4 == 0 :
    print(numero, 'es múltiplo de cuatro y de dos')
else:
    print(numero, 'no es múltiplo de dos')