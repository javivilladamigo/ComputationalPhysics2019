# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('classic')
fig = plt.figure()
fig.patch.set_facecolor('xkcd:white')

prec=1e-5

def f(x):
	y=x**3-3*x**2-x+3
	return y



a=0
b=1.35
n=2
h=(b-a)/n


# evaluo a integral usando un intervalo
integral1=(b-a)/2*(f(a)+f(b))

# evaluo a integral usando dous intervalos (principalmente para facer a avaliación xa con dous elementos no bucle)
integral2=(f(h)+f(a))*h/2+(f(h)+f(b))*h/2

# evaluo a integral dividindoa en trapecios cada vez que a diferencia entre a integral con n+1 intervalos e n, non dea o resultado buscado
while np.abs(integral2-integral1)>prec:
	n+=1
	h=(b-a)/n
	x=np.linspace(a,b,n-1)
	suma=np.sum(f(x))
	integral1=(h/2)*(f(a)+f(b))+h*suma
	n+=1
	h=(b-a)/n
	x=np.linspace(a,b,n-1)
	suma=np.sum(f(x))
	integral2=(h/2)*(f(a)+f(b))+h*suma


# output
print('Regla del trapecio: \n')
print('Precisión: %.6e' % prec)
print('A integral entre a = %.6f e b = %.6f é: %.9f' % (a, b, integral2))


# ploteo
aux=np.linspace(a,b,1000)
plt.clf()
plt.plot(aux,f(aux), color='red')
plt.fill_between(aux, f(aux), color='blue', alpha=0.3)
plt.show()