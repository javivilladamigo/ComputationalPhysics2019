# Javier Mariño
import matplotlib.pyplot as plt
import numpy as np

dimt = 2000 # número de iteraciones temporales
deltat = 0.1; deltax = 0.5; alfa = 0.1; N = 20 # parámetros naturales de la discretización
s = alfa*deltat/deltax**2 # calculamos la estabilidad
t=0; w=0.5 #parámetros para la oscilacion de un foco

T = np.zeros(N+1); np.random.seed(30)
T=10*np.random.rand(N+1);
T[0]=np.sin(w*t)
T[N]=10


plt.close('all')
plt.plot(np.arange(N+1)*deltax,T,'-r'); plt.pause(0.00001)

for n in range(dimt):

	for i in range(1,N):
		T[i] = T[i]+alfa*deltat/deltax**2*(T[i+1]-2.*T[i]+T[i-1])
	T[0]=np.sin(w*t)
	T[N]=10
	t += deltat

	if n%20==0:
		plt.plot(np.arange(N+1)*deltax,T)
		plt.pause(0.00001)
		plt.show()

plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('FTCS con un foco oscilante')