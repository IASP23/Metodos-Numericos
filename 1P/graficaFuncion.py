# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 00:15:08 2021

@author: ASUS I7 10MA
"""

import matplotlib.pyplot as plt
import numpy as np
from sympy import *

x = Symbol('x') #declaramos que x es un simbolo
y = Symbol('y')

x = np.linspace(0,1.5,200) # Crea un arreglo entre 0 y 2 con 200 puntos
y = x*np.exp(-x/3)-0.7  # calcula las imágenes de la función

plt.plot(x,y,'r-.',linewidth = 1) # Grafica la función según los pntos anteriores
plt.xlabel('x') #etiqueta del eje x
plt.ylabel('y') #etiqueta del eje y
plt.title('Gráfica de función') #titulo de la grafica
plt.grid(True) #muestra la cuadricula
plt.axis([0, 1.5, -1, 1]) # intervalos de los ejes de la grafica
plt.show()
