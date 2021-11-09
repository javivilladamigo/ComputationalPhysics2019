# Javier Mariño
## UPWIND CONVECCION ##
import matplotlib.pyplot as plt
import numpy as np

dimt = 100 # número de iteraciones temporales
deltat = 0.01; deltax = 0.5; C = 1.0; u = C*deltax/deltat
N = 200 # parámetros naturales de la discretización

T = np.zeros(N+1); T[5:30]=np.ones(25)*1; #T[N]=10 # vector inicial, con las c.i. que queramos
Tnew = T.copy()

plt.close('all')
plt.plot(np.arange(N+1)*deltax,T,'-r'); plt.pause(0.000001) # primera representacion

for n in range(dimt):

	for i in range(1,N):
		Tnew[i] = T[i]-C*(T[i]-T[i-1]) # calculamos el siguiente vector punto por punto
	T = Tnew.copy()

	#cc##
	T[N]=T[N-1]
	
	if n%1==0:
		#plt.clf()
		plt.plot(np.arange(N+1)*deltax,T) #un plot un poco más discretizado para liberar memoria de python
		plt.pause(0.000001)
		plt.show()

plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('upwind convección')