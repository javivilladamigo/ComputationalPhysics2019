# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:47:23 2020

@author: Martin Otero Lema
"""
import numpy as np
import matplotlib.pyplot as plt
N=50 
dimt=100
sx=0.1
sy=0.2


T=np.zeros((N+1,N+1))
Ts=np.zeros((N+1,N+1))
Tnew=np.zeros((N+1,N+1))

## Condiciones iniciales 

T[13:18,13:18]=100
T[15:16, 15:16]=0
T[13:18,33:38,]=100
T[15:16,35:36,]=0

T[38:40, 18:32]=100

T[36:38, 15:18]=100
T[36:38, 32:35]=100

T[34:36, 12:15]=100
T[34:36, 35:38]=100

T[26:27,17:25]=100



## Matriz A para calcular las columnas en el tiempo asterisco
A=np.identity(N+1)
for i in range(1,N):
    A[i,i]=1+sx
    A[i,i+1]=-sx/2
    A[i,i-1]=-sx/2
    
A1=np.linalg.inv(A)

##  Matriz B para calcular las filas en el tiempo asterisco
B=np.identity(N+1)
for i in range(1,N):
    B[i,i]=1+sy
    B[i,i+1]=-sy/2
    B[i,i-1]=-sy/2
    
B1=np.linalg.inv(B)
plt.close("all")
plt.figure(1) 
plt.title("Ecuación de difusión, método ADI")
plt.imshow(T,cmap="inferno", vmin=0, vmax=100) ; plt.xlabel("y") ; plt.ylabel("x") ; plt.colorbar() ; plt.pause(1.5)
for tiempo in range(dimt):
    for j in range(1,N):
        V=np.ones(N+1)
        for i in range(1,N):
            V[i]=0.5*sy*T[i,j-1]+(1-sy)*T[i,j]+0.5*sy*T[i,j+1]
        V[0]=0
        V[-1]=0
        Ts[:,j]=np.dot(A1,V)

    for i in range(1,N):
        U=np.ones(N+1)
        for j in range(1,N):
            U[j]=0.5*sx*Ts[i-1,j]+(1-sx)*Ts[i,j]+0.5*sx*Ts[i+1,j]
        U[0]=0
        U[-1]=0
        Tnew[i,:]=np.dot(B1,U)
    
    T=np.copy(Tnew)
    if tiempo%10==0:
        plt.figure(1)
        plt.imshow(T,cmap="inferno",vmin=0, vmax=100)
        plt.pause(0.1)
        


