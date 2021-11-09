# Javier Mariño
import matplotlib.pyplot as plt
import numpy as np

dimt = 2500 # número de iteraciones temporales
deltat = 0.1; deltax = 0.5; alfa = 0.1; N = 20 # parámetros naturales de la discretización
s = alfa*deltat/deltax**2 # calculamos la estabilidad


np.random.seed(30); T = np.zeros(N+3); # creo un vector con 2 elementos más de los habituales para poder efectuar la extension a 5 vecinos (se crea una especie de frontera virtual con las mismas condiciones que la real)
T[6:10]=5+5*np.random.sample(4); T[0]=0; T[1]=0; T[N+1]=10; T[N+2]=10

plt.close('all')
plt.plot(np.arange(N+1)*deltax,T[1:N+2],'-r'); plt.pause(0.00001)


for n in range(dimt):

	for i in range(1,N+1):
		T[i]=T[i]+s*(-T[i-2]/12.+4.*T[i-1]/3.-2.5*T[i]+4.*T[i+1]/3.-T[i+2]/12.)
	T[1]=0
	T[N+1]=10 # realizando bien el bucle, sólo tenemos que volver a fijar las cc de la frontera real
	
	if n%20==0:
		plt.plot(np.arange(N+1)*deltax,T[1:N+2],'-'); plt.pause(0.00001) # a la hora de graficar obviamos la frontera virtual
		plt.show()

plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('Centrado en espacio (5 vecinos) y upstream en tiempo (dos niveles)')