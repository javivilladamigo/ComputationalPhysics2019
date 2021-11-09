# -*- coding: utf-8 -*-


# GAUSS SIN PIVOTEO
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# estilo que me gusta de grafica
'''
plt.style.use('classic')
fig = plt.figure()
fig.patch.set_facecolor('xkcd:white')
'''

coef=np.array([[2,-1,1],[-1,1,2],[1,2,-1]], float) # defino a matriz
colindep=np.array([3,7,2], float) # defino a matriz de termos independentes
colindep=colindep.reshape(3,1) # transpoñoa

ampl=np.concatenate((coef,colindep), axis=1) # defino a matriz ampliada concatenando a de coeficientes e a de termos independentes

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

print('A matriz triangular:\n ', ampl) # imprimo os resultados
print('Solución por sustitución regresiva:')

for i in range(len(sol)):
	print('x(%i)= %.2f' % (i+1,sol[i]))