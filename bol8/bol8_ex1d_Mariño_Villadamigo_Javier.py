# Javier Mariño
import matplotlib.pyplot as plt
import numpy as np

dimt = 2500 # número de iteraciones temporales
deltat = 0.1; deltax = 0.5; alfa = 0.1; N = 20 # parámetros naturales de la discretización
s = alfa*deltat/deltax**2 # calculamos la estabilidad

T = np.zeros(N+1)
T[5:9]= 5+5*np.random.sample(4) # aleatorios distribuidos en torno a 5 con desviacion 5
T[0]=T[1]
T[N]=T[N-1]

plt.close('all')
plt.plot(np.arange(N+1)*deltax,T,'-r'); plt.pause(0.00001)

for n in range(dimt):

	for i in range(1,N):
		T[i] = T[i]+alfa*deltat/deltax**2*(T[i+1]-2.*T[i]+T[i-1])
	T[0]=T[1] # condicion de frontera de flujo nulo
	T[N] = T[N-1]

	if n%20==0:
		plt.plot(np.arange(N+1)*deltax,T)
		plt.pause(0.00001)
		plt.show()

plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('FTCS con cond. de Von Neumann')