# -*- coding: utf-8 -*-

import numpy as np

def f(x):
	y=x**3-3*x**2-x+3
	return y

x0=1.2 # defino o punto no que quero calcular a derivada


h=1. # inicializo as h
print (' '*6+'h',' '*10+'ecuacion(10)',' '*3+'ecuacion(16)')
for i in range(11): # calculamos e printeamos á vez os resultados da ecuación
	resultado10=(f(x0+h)-f(x0-h))/(2*h)
	
	resultado16=(-f(x0+2*h)+8*f(x0+h)-8*f(x0-h)+f(x0-2*h))/(12*h)
	
	h=h/10 # fago h cada vez mais pequenos
	print('%.10f \t %.8f \t %.8f' % (h*10,resultado10,resultado16))