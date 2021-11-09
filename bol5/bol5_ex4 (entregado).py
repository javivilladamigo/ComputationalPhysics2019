# -*- coding: utf-8 -*-

import numpy as np
from numpy.random import *

ax = 0 # definimos os extremos da figura para definir o volume
bx = 8
ay = ax
by = 6
N=100 
prec = 1e-2; dif = prec+1 # inicializamos a diferencia que logo dentro do bucle definiremos como a diferenza entre dous xG consecutivos
xG = 0

V = (bx-ax)*(by-ay)


def funciondensidad(x,y): # definimos unha función que sexa 0 no semicírculo que lle falta á figura, e 1 no resto
	r = 2
	if (x-6)**2+y**2<=r**2:
		f = 0
	else:
		f = 1
	return f
def random2puntos(a,b): # definimos unha función que nos dea un número aleatorio entre dous extremos
	x = a + (b-a) * random()
	return x


print(' '*5+ 'N' + ' '*9+ 'xG' + ' '*10 + 'Error x'+ ' '*8+ 'yG'+ ' '*8+ 'Error y'	)
while dif>prec: 
	dm = 0; dm2 = 0; sumax = 0; sumay = 0; sumax2 = 0; sumay2 = 0
	for i in range (N): # este é o bucle alternativa a crear un vector N-dimensional
		x = random2puntos(ax,bx); y = random2puntos(ay, by) # facemos os sumatorios necesarios para o método de Monte Carlo
		dm = dm + funciondensidad(x,y)
		dm2 = dm2 + (funciondensidad(x,y))**2
		sumax = sumax + x*funciondensidad(x,y)
		sumay = sumay + y*funciondensidad(x,y)
		sumax2 = sumax2 + (x*funciondensidad(x,y))**2
		sumay2 = sumay2 + (y*funciondensidad(x,y))**2

	ix = V * sumax / N # calculamos as integrais
	iy = V * sumay / N
	im = V * dm / N

	errordm = V * np.sqrt((((dm2/N)-(dm/N)**2))/N) # e os erros segundo as fórmulas do método
	errorx = V * np.sqrt((((sumax2/N)-(sumax/N)**2))/N)
	errory = V * np.sqrt((((sumay2/N)-(sumay/N)**2))/N)

	xG1=ix/im # calculamos as coordenadas do centro de masas
	yG1=iy/im

	N *= 10
	dif = np.abs(xG1-xG); errorxdef=np.sqrt((errorx/im)**2+(ix*errordm/(im**2))**2); errorydef=np.sqrt((errory/im)**2+(iy*errordm/(im**2))**2) # definimos a diferenza entre os dous xG, e facemos a propagación de incertezas
	
	# output
	print(('%8d'+' '*2+'|'+' '*2+'%f'+' '*2+'|'+' '*2+'%f'+' '*2+'|'+' '*2+'%f'+' '*2+'|'+' '*2+'%f')%(N,xG1,errorxdef,yG1,errorydef))
	# reseteamos xG e yG aos novos valores conseguidos
	xG = xG1; yG = yG1


