# Javier Mariño
## CRANK-NICOLSON TRANSPORTE ##
import matplotlib.pyplot as plt
import numpy as np

dimt = 1000 # número de iteraciones temporales
deltat = 0.01; deltax = 0.5; 
C = 0.1; alpha = 1.0
u = C*deltax/deltat 
s = alpha*deltat/deltax**2
N = 200 # parámetros naturales de la discretización

T = np.zeros(N+1);
#np.random.seed(8); 
T[6:10]=5


plt.close('all')
plt.plot(np.arange(N+1)*deltax,T,'-r'); plt.pause(0.00001)

A = np.zeros((N+1,N+1))


for i in range(1,N): # creamos la matriz de coeficientes de Tnew
		for j in range(1,N):
			if i==j:
				A[i,j]=1+s
				A[i,j+1]=-s/2.+C/4.
				A[i,j-1]=-s/2.-C/4.
A[0,0]=1.; A[N,N]=1.
#A[1,N]=1.; A[N-1,N]=1

B = np.zeros((N+1,N+1))

for i in range(1,N):
	for j in range(1,N):
		if i==j:
			B[i,j]=1-s
			B[i,j+1]=-C/4.+s/2.
			B[i,j-1]=C/4.+s/2.

#B[N-1,N]=1; B[1,N]=1
B[0,0] = 1; B[N,N]=1

Ai = np.linalg.inv(A)
D = np.dot(Ai, B)


for n in range(dimt):

	Tnew = np.dot(D,T)
	Tnew[N]=Tnew[N-1];


	if n%10==0:
		plt.plot(np.arange(N+1)*deltax, Tnew,'-'); plt.pause(0.00001)
		plt.show()

	T = Tnew.copy()

			


plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('Crank Nicolson Transporte')