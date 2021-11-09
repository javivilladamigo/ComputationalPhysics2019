# Javier Mariño
## FTCS convección #
import matplotlib.pyplot as plt
import numpy as np

dimt = 1500 # número de iteraciones temporales
deltat = 0.1; deltax = 0.5; N = 20 # parámetros naturales de la discretización
u = 0.01
C = u*deltat/deltax

T = np.zeros(N+1); T[5:9]=np.random.sample(4)*10; #T[N]=10 # vector inicial, con las c.i. que queramos
Tnew = T.copy()

plt.close('all')
plt.plot(np.arange(N+1)*deltax,T,'-r'); plt.pause(0.00001) # primera representacion
plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('FTCS convección (incond. inestable)')

for n in range(dimt):

	for i in range(1,N):
		Tnew[i] = T[i]-0.5*C*(T[i+1]-T[i-1]) # calculamos el siguiente vector punto por punto
	T = Tnew.copy()
	T[N] = T[N-1]
	
	if n%20==0:
		plt.plot(np.arange(N+1)*deltax,T) #un plot un poco más discretizado para liberar memoria de python
		plt.pause(0.00001)
		plt.show()

