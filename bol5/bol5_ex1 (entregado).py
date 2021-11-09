# -*- coding: utf-8 -*-

import numpy as np
from numpy.random import *

def f(x): # definimos a funcion
	y=(1-x**2)**1.5
	return y

a = 0 # definimos os limites do intervalo
b = 1
V = b-a # e o volume de integración (neste caso 1D)
N = 10 # definimos un primeiro valor para a cantidade de números aleatorios 
prec = 1e-4 # definimos a precisión

suma = 0 # inicializamos a suma e a suma de cadrados
suma_cuad = 0

for i in range(N): # facemos este bucle como alternativa a crear un vector N-dimensional. O aforro en memoria resulta evidente xa que só almacenamos un dato cada vez en lugar dun vector de N elementos, pero o proceso de execución ralentízase notablemente

	x = random()

	f_media = suma + (1/N)*f(x)
	f_media_cuadrado =  suma_cuad + (1/N)*(f(x)**2)

integral = V * f_media # primeiro valor da integral (poderíase prescindir del)


error = V * np.sqrt((f_media_cuadrado-f_media**2)/N) # calculamos o primeiro erro


while np.abs(error)>prec: # inicializamos o bucle no que mentres o erro sexa maior que precisión, repetimos o proceso aumentando N

	N = N*10
	f_media = 0
	f_media_cuadrado = 0

	for i in range(N):
		x = random()
		f_media = f_media + (1/N)*f(x)
		f_media_cuadrado = f_media_cuadrado + (1/N)*(f(x))**2

	error = V * np.sqrt((f_media_cuadrado-f_media**2)/N)

integral = V * f_media # resultado final

# output
print('A integral entre %f e %f da función é: %.10f' % (a,b,integral))
print('Erro: %.2e' % (error))



