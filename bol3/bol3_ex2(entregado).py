# -*- coding: utf-8 -*-

import numpy as np
from math import *



n=2
h=0.01
x0=1.2

b=np.arange(-n,n+1,1) # definimos o rango de b

def f(x): # definimos a función
	y=x**3-3*x**2-x+3
	return y

A=np.zeros((2*n+1,2*n+1), float)

derivada=[]
print('Derivada por coeficientes indeterminados \n')
print('Evalúa a función en %.i puntos: \n' % (2*n+1))
print('xo+h*',b)
print()

for k in range(1,3+1,1):
	colindep=np.zeros((2*n+1,1)) # definimos a columna de termos independentes onde o elemento k-esimo é k!
	colindep[k,0]=factorial(k)

	for i in range(2*n+1): # definimos a matriz de coeficientes que precisamos para o metodo de coeficientes indeterminados
		A[i,:]=b**i

	ampl=np.concatenate((A,colindep), axis=1) # defino a matriz ampliada concatenando a de coeficientes e a de termos independentes

	F,C = np.shape(ampl) # asigno a F e C as dimensions da matriz ampliada

	for j in range(0,F): # fago a matriz triangular superior
		for i in range(j+1,F):
			ampl[i,:]=ampl[i,:]-ampl[j,:]*(ampl[i,j]/ampl[j,j])



	sol=np.zeros((F,1),float) # designo unha columna de solucións e soluciono o sistema por substitución regresiva
	for i in range(F-1,-1,-1): 
		suma=0
		for j in range(F):
			suma+=ampl[i,j]*sol[j,0]
		sol[i,0]=(ampl[i,C-1]-suma)/ampl[i,i]

	funcion=f(x0+b*h) # defino o valor da función dependente dos parámetros b e h
	a=sol.transpose() #  fago a matriz de solucions horizontal
	derivada=(np.dot(a,funcion))/(h**k) # calculo a derivada k-esima
	print('A derivada de orden %i en x0 = %.6f é: %.6f' % (k,x0,derivada))