# -*- coding: utf-8 -*-


# REGULA-FALSI
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# estilo que me gusta de grafica
'''
plt.style.use('classic')
fig = plt.figure()
fig.patch.set_facecolor('xkcd:white')
'''
def funcion(x):
	y=x**2-3*x+np.exp(x)-2
	return y

xplot=np.linspace(-2,4,100) #defino este vector para plotear mas suave la funcion
plt.clf()
plt.axhline(0,color='k',xmin=-2,xmax=4)
y=funcion(xplot)
plt.plot(xplot,y)

x1=np.linspace(-0.5,-0.2,10)
x1intersec=x1[0]-funcion(x1[0])*(x1[len(x1)-1]-x1[0])/(funcion(x1[len(x1)-1])-funcion(x1[0]))

x2=np.linspace(1.3,1.6,10)
x2intersec=x2[0]-funcion(x2[0])*(x2[len(x2)-1]-x2[0])/(funcion(x2[len(x2)-1])-funcion(x2[0]))


soluciones=[]
prec=1e-5

# bucle para el primer intervalo
while np.abs(funcion(x1intersec))>=prec:
	if np.sign(funcion(x1intersec))!=np.sign(funcion(x1[0])):
		x1=np.linspace(x1[0],x1intersec,10)
		x1intersec=x1[0]-funcion(x1[0])*(x1intersec-x1[0])/(funcion(x1intersec)-funcion(x1[0]))
	else:
		x1=np.linspace(x1intersec,x1[len(x1)-1],10)
		x1intersec=x1intersec-funcion(x1intersec)*(x1[len(x1)-1]-x1intersec)/(funcion(x1[len(x1)-1])-funcion(x1intersec))
if np.abs(funcion(x1intersec))<=prec:
	soluciones.append(x1intersec)

# bucle para el segundo intervalo
while np.abs(funcion(x2intersec))>=prec:
	if np.sign(funcion(x2intersec))!=np.sign(funcion(x2[0])):
		x2=np.linspace(x2[0],x2intersec,10)
		x2intersec=x2[0]-funcion(x2[0])*(x2intersec-x2[0])/(funcion(x2intersec)-funcion(x2[0]))
	else:
		x2=np.linspace(x2intersec,x2[len(x2)-1],10)
		x2intersec=x2intersec-funcion(x2intersec)*(x2[len(x2)-1]-x2intersec)/(funcion(x2[len(x2)-1])-funcion(x2intersec))
if np.abs(funcion(x2intersec))<=prec:
	soluciones.append(x2intersec)


print('Regula-Falsi:')
print('x1 = %.6f f(x1) = %.6f' % (x1intersec,funcion(x1intersec)))
print('x2 = %.6f f(x2) = %.6f' % (x2intersec,funcion(x2intersec)))



