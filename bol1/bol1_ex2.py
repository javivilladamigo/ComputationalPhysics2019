# -*- coding: utf-8 -*-


# BISECCION
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

# usando os resultados do exercicio e podemos empregar os intervalos que xa obtivemos
soluciones=[]
prec=1 # !!!!!! de momento con mas precision peta totalmente

x=np.linspace(-2,4,21)

rango=[] #inicializo la matriz donde almaceno los intervalos
for i in range(len(x)):
	if np.sign(funcion(x[i-1]))!=np.sign(funcion(x[i])):
		rango.append(x[i-1])
		rango.append(x[i])



#primer intervalo
x1=np.linspace(rango[0],rango[1],100)
x1med=(x1[0]+x1[len(x1)-1])/2

while np.abs(funcion(x1med))>prec:
	if np.sign(funcion(x1[0]))!=np.sign(funcion(x1med)):
		x1med=(x1[0]+x1med)/2
		x1=np.linspace(x1[0],x1med,10)
	else:
		x1med=(x1med+x1[len(x1)-1])/2
		x1=np.linspace(x1med,x1[len(x1)-1],10)
if np.abs(funcion(x1med))<=prec:
	soluciones.append(x1med)


#segundo intervalo
x2=np.linspace(rango[2],rango[3],100)
x2med=(x2[0]+x2[len(x2)-1])/2

while np.abs(funcion(x2med))>prec:
	if np.sign(funcion(x2[0]))!=np.sign(funcion(x2med)):
		x2med=(x2[0]+x2med)/2
		x2=np.linspace(x2[0],x2med,10)
	else:
		x2med=(x2med+x2[len(x2)-2])/2
		x2=np.linspace(x2med,x2[len(x2)-1],10)
if np.abs(funcion(x2med))<=prec:
	soluciones.append(x2med)



print('Bisección:')
print('x1 = %.6f f(x1) = %.6f' % (x1med,funcion(x1med)))
print('x2 = %.6f f(x2) = %.6f' % (x2med,funcion(x2med)))


plt.clf()
plt.axhline(0,color='k',xmin=-2,xmax=4)
xplot=np.linspace(-2,4,100) #defino este vector para plotear mas suave la funcion
y=funcion(xplot)
plt.plot(xplot,y)
plt.axvline(x1med, color='r')
plt.show()

