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

for i in range(1,N): # creamos la matriz de coeficientes de Tnew
		for j in range(1,N):
			if i==j:
				A[i,j]=1+s
				A[i,j+1]=-s/2
				A[i,j-1]=-s/2
A[0,0]=1.; A[N,N]=1

B = np.zeros((N+1,N+1))

for i in range(1,N): # a diferencia de FTCS, necesitamos crear los coeficientes de los Told
		for j in range(1,N):
			if i==j:
				B[i,j]=1-s
				B[i,j+1]=s/2
				B[i,j-1]=s/2
B[0,0]=1.; B[N,N]=1

Bi = np.linalg.inv(B)
C = np.linalg.inv(np.dot(Bi,A)) # despejamos la ecuacion

for n in range(dimt):

	Tnew = np.dot(C,T) # y calculamos los Tnew
	Tnew[N]=10; Tnew[0]=0

	if n%20==0:
		plt.plot(np.arange(N+1)*deltax,Tnew,'-'); plt.pause(0.00001)
		plt.show()

	T = Tnew

plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('Crank-Nicolson')