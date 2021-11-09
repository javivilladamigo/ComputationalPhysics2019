# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('classic')
fig = plt.figure()
fig.patch.set_facecolor('xkcd:white')

def f(x): # definimos a función da que queremos coñecer a integral
    y=(x**2+x+1)*np.cos(x)
    return y

def T(f,a,b,j): # definimos a regra recuesiva do trapecio
    T=(b-a)/2*(f(a)+f(b)) # definimos o primeiro termo da serie
    for k in range(2,j+2): # e os termos recurrentes segundo a expresión (12)
        h=(b-a)/(2**(k-1))
        i=np.arange(1,2**(k-2)+1)
        x2=a+((2*i)-1)*h
        T=(T/2)+(h*sum(f(x2)))
    return T

a=0 # definimos o intervalo, o numero de melloras da iteración, e a precisión
b=np.pi/2
N=5
prec=1e-8

def R(a,b,N): # isto é análogo ao anterior pero usámolo para imprimir a matriz
    R=np.zeros((N,N))
    for j in range (N):
        R[j,0]=T(f,a,b,j)
    
    for k in range (1,N):
        for j in range(k,N):
            R[j,k]=(((4**k)*R[j,k-1])-R[j-1,k-1])/((4**k)-1) #le quitamos los -1 en las exponenciales porque en phython las cosas empiezan en cero
    
    return R

def Rn(a,b,N): # definimos a matriz de Romberg que nos dará as sucesivas iteracións en j (devolvemos o último elemento) que é presumiblemente o máis preciso
    R=np.zeros((N,N))
    for j in range (N):
        R[j,0]=T(f,a,b,j)
    
    for k in range (1,N):
        for j in range(k,N):
            R[j,k]=(((4**k)*R[j,k-1])-R[j-1,k-1])/((4**k)-1)
    
    sol=R[N-1,N-1]
    return sol
    
while abs(Rn(a,b,N+1)-Rn(a,b,N))>prec: # iteramos ata que a solución teña a precisión desexada
    N=N+1

#output
print('\n')
print('R(j,1),'+' '*6+'R(j,2),'+' '*4+'R(j,3),'+' '*4+'R(j,4),'+' '*4+'R(j,5)')
print(R(a,b,5))
print('\n')
print("Regla recursiva de Romberg:")
print('\n')
print("Precisión: %.6e" % (prec))
print("A integral entre a = %f e b = %f é: %.12f" % (a, b, Rn(a,b,N)))

aux=np.linspace(a,b,1000)
plt.clf()
plt.plot(aux, f(aux), color='red')
plt.fill_between(aux, f(aux), color='blue', alpha='0.3')
plt.show()
