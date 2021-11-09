#Javier Mariño
## ADI ##
import matplotlib.pyplot as plt
import numpy as np


dimt = 500; deltat = 0.1; N = 50 # parámetros naturales de la discretización
deltax = 0.5; alphax = 1; sx = alphax*deltat/deltax**2
deltay = 0.5; alphay = 1; sy = alphay*deltat/deltay**2


# creamos los vectores en cada tiempo #
T = np.zeros((N+1, N+1));
Tnew = T.copy()
Tast= T.copy();



T[20:30,20:30] = 10 # c inicial

'''
for i in range(1,N):
	for j in range(1,N):
		T[i,j]=10
'''

plt.close('all')
plt.imshow(T, cmap='hot')
plt.colorbar()
plt.pause(0.1)
plt.show()

Aast = np.zeros((N+1, N+1))
Bast = np.zeros((N+1, N+1))


# creamos las matrices para calcular el paso de n a *
for i in range(1,N): 
		for j in range(1,N):
			if i==j:
				Aast[i,j]=1+sx
				Aast[i,j+1]=-sx/2.
				Aast[i,j-1]=-sx/2.
Aast[0,0]=1.; Aast[N,N]=1.

for i in range(1,N):
	for j in range(1,N):
		if i==j:
			Bast[i,j]=1+sy
			Bast[i,j+1]=-sy/2.
			Bast[i,j-1]=-sy/2.
Bast[0,0]=1.; Bast[N,N]=1.

Aastinv = np.linalg.inv(Aast); Bastinv = np.linalg.inv(Bast)
# Cast = np.dot(Aastinv, Bast) # no hace falta en este caso, el paso explícito se hace por columnas (en y) o por filas (en x)

for n in range(dimt):


	pasoy = np.zeros(N+1)
	for j in range(1,N):
		for i in range(1,N):
			# calculo explícitamente el paso en y a *	
			pasoy[i] = sy/2.*T[i,j-1]+(1-sy)*T[i,j]+sy/2.*T[i,j+1]
		# construyo el T* por columnas
		Tast[:,j] = np.dot(Aastinv, pasoy)


	pasox = np.zeros(N+1)
	for i in range(1,N):
		for j in range(1,N):
			# calculo explicitamente el paso en x a n+1	
			pasox[j] = sx/2.*Tast[i-1,j]+(1-sx)*Tast[i,j]+sx/2.*Tast[i+1,j] # no tengo muy claro si el factor que va con ij es 1-sx o 1-2sx pero con el primero la difusión es simétrica
		# construyo el Tnew por filas
		Tnew[i,:] = np.dot(Bastinv, pasox)

	T = Tnew.copy()

	## cc de von neumann ##
	T[0,:] = T[1,:]
	T[N,:] = T[N-1,:]
	T[:,0] = T[:,1]
	T[:,N] = T[:,N-1]

	if n%50==0:
		plt.imshow(T, cmap='hot')
		plt.pause(0.00000000001)
		plt.show()

plt.xlabel('$x$')
plt.ylabel('$y$')



			


