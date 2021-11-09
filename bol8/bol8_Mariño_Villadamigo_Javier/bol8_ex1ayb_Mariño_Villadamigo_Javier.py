# Javier Mariño
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import uniform

dimt = 2000 # número de iteraciones temporales
deltat = 0.1; deltax = 0.5; alfa = 0.1; N = 20 # parámetros naturales de la discretización
s = alfa*deltat/deltax**2 # calculamos la estabilidad

T = np.zeros(N+1); T[6:10]=5+5*np.random.sample(4); T[N]=10 # vector inicial, con las c.i. que queramos

plt.close('all')
plt.plot(np.arange(N+1)*deltax,T,'-r'); plt.pause(0.00001) # primera representacion

for n in range(dimt):

	for i in range(1,N):
		T[i] = T[i]+alfa*deltat/deltax**2*(T[i+1]-2.*T[i]+T[i-1]) # calculamos el siguiente vector punto por punto
	T[0]=0 #aplicamos cc
	T[N]=10
	
	if n%20==0:
		plt.plot(np.arange(N+1)*deltax,T) #un plot un poco más discretizado para liberar memoria de python
		plt.pause(0.00001)
		plt.show()

plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('FTCS')