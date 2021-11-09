# Javier Mariño
## dos niveles implicito conveccion ##
import matplotlib.pyplot as plt
import numpy as np

dimt = 400 #número de iteraciones temporales
deltat = 0.01; deltax = 0.5; C = 1.0; u = C*deltax/deltat
N = 200 # parámetros naturales de la discretización

T = np.zeros(N+1);
T[6:10]=5


plt.close('all')
plt.plot(np.arange(N+1)*deltax,T,'-r'); plt.pause(0.00001)

A = np.zeros((N+1,N+1))


for i in range(1,N): # creamos la matriz de coeficientes de Tnew
		for j in range(1,N):
			if i==j:
				A[i,j]=1.
				A[i,j+1]=0.5*C
				A[i,j-1]=-0.5*C
A[0,0]=1.; A[N,N]=1.


B = np.zeros((N+1,N+1))

for i in range(1,N): # a diferencia de FTCS, necesitamos crear los coeficientes de los Told
		for j in range(1,N):
			if i==j:
				B[i,j]=1
B[0,0]=1.; B[N,N]=1.

Ai = np.linalg.inv(A)
C = np.dot(Ai,B) # despejamos la ecuacion


for n in range(dimt):

	Tnew = np.dot(C,T)
	Tnew[N]=Tnew[N-1];


	#Tnew[N] = (Tnew[N-1]+Tnew[N])/2	
	
	if n%10==0:
		#plt.clf()
		plt.plot(np.arange(N+1)*deltax, Tnew,'-'); plt.pause(0.00001)
		plt.show()
		

	T = Tnew.copy()

plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('dos niveles implícito')