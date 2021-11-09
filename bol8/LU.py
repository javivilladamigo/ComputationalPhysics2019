# -*- coding: utf-8 -*-


import numpy as np


def LU(U,b):

	F,C=np.shape(U)

	L=np.zeros((F,C))

	P=np.identity(F) # para un caso máis xeral poderiamos usar eye

# inicializamos un vector onde almacenaremos as posicións dos pivotes
	pivote=np.arange(C)

	for j in range(C-1): # facemos o pivoteo nas matrices U, L e P (bucle j) e eliminación (bucle i)
		
		pivote[j]=np.argmax(np.fabs(U[:,j])) # pivoteo en U
		auxU=U[pivote[j],:].copy()
		U[pivote[j],:]=U[j,:]
		U[j,:]=auxU

		auxL=L[pivote[j],:].copy() # pivoteo en L
		L[pivote[j],:]=L[j,:]
		L[j,:]=auxL

		auxP=P[pivote[j],:].copy() # pivoteo en P
		P[pivote[j],:]=P[j,:]
		P[j,:]=auxP


		for i in range(j+1,F):
			L[i,j]=U[i,j]/U[j,j]
			U[i,:]=U[i,:]-L[i,j]*U[j,:]

	for i in range(F): # engadimos 1 na diagonal ppal de L (52)
		L[i,i]+=1

	Pb=np.dot(P,b) # calculamos o produto P*b (53)

	soly=np.zeros((F,1),float) # designo unha columna de solucións para y

	for i in range(F): # resolvemos soly por substitucion progresiva (54)
		suma=0
		for j in range(i):
			suma+=L[i,j]*soly[j,0]
		soly[i,0]=(Pb[i,0]-suma)/L[i,i]


		solx=np.zeros((F,1),float) # designo unha columna de solucións para x e soluciono o sistema por substitución regresiva (56)
		for i in range(F-1,-1,-1): 
			suma=0
			for j in range(F):
				suma+=U[i,j]*solx[j,0]
			solx[i,0]=(soly[i,0]-suma)/U[i,i]

	return (L,U,P,solx)

'''
#output
print()
print('Método factorización LU con pivoteo parcial\n')
print('Matriz triangular inferior L:')
print(L, '\n')
print('Matriz triangular superior U:')
print(U, '\n')
print('Matriz de permutación P:')
print(P, '\n')
print('Solución por factorización LU:')
for i in range(len(solx)):
	print('x(%i)= %.6f' % (i+1,solx[i]))

'''