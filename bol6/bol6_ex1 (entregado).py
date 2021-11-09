# -*- coding: utf-8 -*-

import numpy as np

A = np.array([[3,-1,0],[-1,2,-1],[0,-1,3]], 'float'); F,C = np.shape(A)

D = np.copy(A) # definimos as matrices desexadas
V = np.identity(F)

erroraux = True  # inicializamos o método de comparación

prec = 1e-7 # precisión desexada
while erroraux:


    p = 0; q = 0; z = 0 # buscamos el elemento máximo de D
    for i in range(F):
        for j in range(C):
            if np.abs(D[i,j])>z and i!=j:
                z = np.abs(D[i,j])
                p = i; q = j

    theta = (D[q,q]-D[p,p])/(2*D[p,q]) # definimos theta

    if theta>=0: # definimos o signo de theta e con el, t
        signo = 1
    else:
        signo = -1
    t = signo/(np.abs(theta)+np.sqrt(theta**2+1))

    c = 1/np.sqrt(t**2+1) # definimos c

    s = c*t # definimos s

    R = np.identity(F); R[p,p] = c; R[p,q] = s; R[q,p] = -s; R[q,q] = c # creamos R e cambiamos os elementos desexados
    RT = np.copy(R) # creo unha copia de R onde alamceno a transposta

    for i in range(F): # creamos a matriz transposta de R
        for j in range(C):
            RT[i,j] = R[j,i]

    D1 = np.dot(RT, np.dot(D, R)) # elaboramos as novas matrices
    V1 = np.dot(V,R)

    erroraux=(np.any(np.abs(D1-D)>prec)) # mentres un elemento da matriz D non converxa coa precisión desexada repetimos o proceso
    

    D = D1; V = V1 # reiniciamos as matrices para só ter dúas almacenadas de cara á comparación

# output

print ('\nMétodo de Jacobi:\n')
print ('Precisión: %1.e \n' % (prec))
print ('Autovalores: \n')
print (np.diag(D),'\n')
print ('Autovectores (en columnas): \n')
with np.printoptions(precision=8, suppress=True):
    print(V)



