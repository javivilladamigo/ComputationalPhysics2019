# Javier Mariño
import matplotlib.pyplot as plt
import numpy as np

dimt = 2500 # número de iteraciones temporales
deltat = 0.1; deltax = 0.5; alfa = 0.1; N = 20 # parámetros naturales de la discretización
s = alfa*deltat/deltax**2 # calculamos la estabilidad

T = np.zeros(N+1);
np.random.seed(8); T[6:10]=5+5*np.random.sample(4); T[0]=0; T[N]=10


plt.close('all')
plt.plot(np.arange(N+1)*deltax,T,'-r'); plt.pause(0.00001)

A = np.zeros((N+1,N+1))
T=T.reshape(N+1,1);

for i in range(1,N): # creamos la matriz A 
		for j in range(1,N):
			if i==j:
				A[i,j]=1+2*s
				A[i,j+1]=-s
				A[i,j-1]=-s
A[0,0]=1.; A[N,N]=1

Ai = np.linalg.inv(A) # invertimos

for n in range(dimt):

	Tnew = np.dot(Ai,T)
	Tnew[N]=10; Tnew[0]=0 

	if n%20==0:
		plt.plot(np.arange(N+1)*deltax, Tnew,'-'); plt.pause(0.00001)
		plt.show()

	T = Tnew

plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('FTCS implícito')