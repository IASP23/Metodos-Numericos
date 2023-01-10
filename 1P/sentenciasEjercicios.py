capacidadTanque = float(input('Capacidad del tanque: '))
costoGasolina = float(input('Costo de la gasolina: '))
costoDiesel = float(input('Costo del diesel: '))
cantidadDinero = float(input('Cuanto dinero tiene: '))
consumeCarro =0
seleccion = int(input('1. Gasolina \n 2.Diesel \n'))

if seleccion == 1 :
    consumeCarro =costoGasolina * capacidadTanque 
    if cantidadDinero >= consumeCarro:
        print('Puede llenar el tanque completo')
    elif cantidadDinero < consumeCarro :
        print ('Puede llenar medio tanque')
else :
     consumeCarro =costoDiesel * capacidadTanque 
     if cantidadDinero >= consumeCarro:
        print('Puede llenar el tanque completo')
     elif cantidadDinero < consumeCarro :
        print ('Puede llenar medio tanque')