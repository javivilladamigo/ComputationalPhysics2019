# Javier Mariño
import matplotlib.pyplot as plt
import numpy as np

dimt = 40000 # número de iteraciones temporales
deltat = 1e-4; deltax = 0.1; alfa = 1.; N = 20 # parámetros naturales de la discretización
s = alfa*deltat/deltax**2 # calculamos la estabilidad
t=0; w=1. #parámetros para la oscilacion de un foco

T = np.zeros(N+3); # creo un vector con 2 elementos más de los habituales para poder efectuar la extension a 5 vecinos (se crea una especie de frontera virtual con las mismas condiciones que la real)
T[6:10]=10; T[0]=0; T[1]=0; T[N+1]=5*np.sin(w*t); T[N+2]=5*np.sin(w*t)
Tnew = T.copy()

plt.close('all')
plt.plot(np.arange(N+1)*deltax,T[1:N+2],'-r'); plt.pause(0.0000001)

for n in range(dimt):

	for i in range(1,N+1):
		Tnew[i]=T[i]+s*(-T[i-2]+16.*T[i-1]-30*T[i]+16.*T[i+1]-T[i+2])
	Tnew[1]=0
	Tnew[N+1]=5*np.sin(w*t);
	Tnew[N+2]=5*np.sin(w*t);
	T = Tnew.copy()
	t += deltat

	if n%100==0:
		plt.plot(np.arange(N+1)*deltax,T[1:N+2],'-'); plt.pause(0.00000001) # a la hora de graficar obviamos la frontera virtual
		plt.show()

plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('FTCS con un foco oscilante')