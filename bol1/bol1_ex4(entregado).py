# -*- coding: utf-8 -*-


# NEWTON-RAPHSON	
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# estilo que me gusta de grafica

plt.style.use('classic')
fig = plt.figure()
fig.patch.set_facecolor('xkcd:white')

def funcion(x): # definimos a funcion a analizar
	y=x**2-3*x+np.exp(x)
	return y
def derivada(x): # definimos a derivada (ainda que se poderia facer mais sinxelo con lambdify)
	y=2*x-3+np.exp(x)
	return y


rango=[] # inicializo a matriz onde almaceno os intervalos nos que haberá ceros

x=np.linspace(-2,4,21) # divido o rango de estudo en 20 intervalos
xplot=np.linspace(-2,4,100) # defino este vector para plotear mais suave a funcion
y=funcion(xplot)


for i in range(len(x)): # para cada extremo do intervalo evaluamos o signo da funcion e almacenamos os puntos na matriz rango se a funcion cambia de signo nos extremos
	if np.sign(funcion(x[i-1]))!=np.sign(funcion(x[i])):
		rango.append(x[i-1])
		rango.append(x[i])





x1sol=(-2-funcion(-2)/derivada(-2)) # fago a primeira iteración do método partindo de x=-2

x2sol=(1.3-funcion(1.3)/derivada(1.3)) # analogamente para x2

soluciones=[] # inicializo o vector de solucións no que almacenarei os puntos que converxan ata unha determinada precisión á solución
prec=1e-5 # defino a precisión coa que quero a solución

while np.abs(funcion(x1sol))>=prec: # itero newton ata que a funcion(x*)<precision 
	x1sol=x1sol-funcion(x1sol)/derivada(x1sol)
if np.abs(funcion(x1sol))<=prec:
	soluciones.append(x1sol)

while np.abs(funcion(x2sol))>=prec: # analogamente para o segundo intervalo
	x2sol=x2sol-funcion(x2sol)/derivada(x2sol)
if np.abs(funcion(x2sol))<=prec:
	soluciones.append(x2sol)

# SAIDA
print('Os intervalos nos que hai ceros: (%g,%g) e (%g,%g)' % (rango[0],rango[1],rango[2],rango[3]))
print('A funcion nos limites dos intervalos vale: (%.6f,%.6f) e (%.6f,%.6f)' % (funcion(rango[0]),funcion(rango[1]),funcion(rango[2]),funcion(rango[3])))

print('Newton-Raphson:')
print('x1 = %.6f f(x1) = %.6f' % (x1sol,funcion(x1sol)))
print('x2 = %.6f f(x2) = %.6f' % (x2sol,funcion(x2sol)))


# grafico
plt.clf()
plt.axhline(0,color='k',xmin=-2,xmax=4)
plt.axvspan(rango[0], rango[1], alpha=0.3, color='g', label='Intervalos con cero')
plt.axvspan(rango[2], rango[3], alpha=0.3, color='g')
plt.plot(xplot,y, label= 'Funcion')
plt.axvline(x1sol, color='r',label='Ceros'); plt.axvline(x2sol, color='r')
plt.legend(loc='best')
plt.show()