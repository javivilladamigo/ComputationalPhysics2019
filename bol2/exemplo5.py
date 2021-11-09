# -*- coding: utf-8 -*-


import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

U=np.array([[1,2,-1],[2,4,5],[3,-1,-2]], float)
L=np.zeros((3,3))
P=np.identity(3) # para un caso más general podemos usar eye
b=np.array([[2],[25],[-5]],float)

# ahora tenemos que realizar el pivoteo
F,C=np.shape(U)

pivote=[]
pivote.append(np.argmax(U[:,0])) # encuentro el pivote de la primera columna y lo almaceno
auxU=U[pivote[0],:].copy() # guardo la fila del pivote en un elemento auxiliar
U[pivote[0],:]=U[0,:] # paso la primera fila a la fila del pivote
U[0,:]=auxU # cambio la primera fila por la fila del pivote

# estos cambios los tengo que realizar también en las matrices L y P

## L ##
auxL=L[pivote[0],:].copy() # guardo la fila del pivote en un elemento auxiliar
L[pivote[0],:]=L[0,:] # paso la primera fila a la fila del pivote
L[0,:]=auxL # cambio la primera fila por la fila del pivote

## P ##
auxP=P[pivote[0],:].copy() # guardo la fila del pivote en un elemento auxiliar
P[pivote[0],:]=P[0,:] # paso la primera fila a la fila del pivote
P[0,:]=auxP # cambio la primera fila por la fila del pivote



# comenzamos el proceso de eliminacion por el pivote U_11
m21=U[1,0]/U[0,0]
U[1,:]=U[1,:]-m21*U[0,:]
m31=U[2,0]/U[0,0]
U[2,:]=U[2,:]-m31*U[0,:]

# sustituimos los elementos L_21 por m_21 y L_31 por m_31
L[1,0]=m21
L[2,0]=m31

# como U_22>U32 no hace falta realizar pivoteo
# realizamos el proceso de eliminación por el pivote U_22
m32=U[2,1]/U[1,1]
U[2,:]=U[2,:]-m32*U[1,:]

# volvemos a sustituir el elemento ij de L por el multiplicador ij
L[2,1]=m32
for i in range(F): # añadimos un uno en la diagonal principal
	for j in range (C):
		if i==j:
			L[i,j]=L[i,j]+1

# calculemos el producto Pb
Pb=np.dot(P,b)

# planteando Ly=Pb, debemos obtener las soluciones de y
y=[]
y1=-5
y2=25-2/3*y1
y3=2-1/2*y2-1/3*y1
y.append(y1); y.append(y2); y.append(y3)

# ahora resolvemos Ux=y
x3=y[F-1]/U[2,2]
x2=(y[F-2]-U[1,2]*x3)/U[1,1]
x1=(y[F-3]-U[0,2]*x3-U[0,1]*x2)/U[0,0]