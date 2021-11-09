# -*- coding: utf-8 -*-

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# estilo que me gusta de grafica
plt.style.use('classic')
fig = plt.figure()
fig.patch.set_facecolor('xkcd:white')


def funcion(x):
	y=x**2-3*x+np.exp(x)-2
	return y

xplot=np.linspace(-2,4,100) #defino este vector para plotear mas suave la funcion
x=np.linspace(-2,4,21)
y=funcion(xplot)

plt.clf()
plt.axhline(0,color='k',xmin=-2,xmax=4)
plt.plot(xplot,y)

rango=[] #inicializo la matriz donde almaceno los intervalos

for i in range(len(x)): # compruebo en qué límites de intervalo la función cambia de signo
	if np.sign(funcion(x[i-1]))!=np.sign(funcion(x[i])):
		rango.append(x[i-1])
		rango.append(x[i])
plt.axvspan(rango[0], rango[1], alpha=0.3, color='r')
plt.axvspan(rango[2], rango[3], alpha=0.3, color='r')
plt.show()



print('Os intervalos son: (%g,%g) e (%g,%g)' % (rango[0],rango[1],rango[2],rango[3]))
print('A funcion nos limites dos intervalos vale: (%.6f,%.6f) e (%.6f,%.6f)' % (funcion(rango[0]),funcion(rango[1]),funcion(rango[2]),funcion(rango[3])))



