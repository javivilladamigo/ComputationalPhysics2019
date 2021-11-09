# Javier Mariño 
## FTCS DE TRANSPORTE ##
import matplotlib.pyplot as plt
import numpy as np

dimt = 2000 # número de iteraciones temporales
deltat = 0.1; deltax = 0.5; N = 200; # parámetros naturales de la discretización
C = 0.25; alpha = 0.1
u = C*deltax/deltat 
s = alpha*deltat/deltax**2

T = np.zeros(N+1); T[5:9]=1; #T[N]=10 # vector inicial, con las c.i. que queramos
Tnew = T.copy()

plt.close('all')
plt.plot(np.arange(N+1)*deltax,T,'-r'); plt.pause(0.00001) # primera representacion

for n in range(dimt):

	for i in range(1,N):
		Tnew[i] = -C/2.*(T[i+1]-T[i-1])+s*(T[i-1]-2*T[i]+T[i+1])+T[i]# calculamos el siguiente vector punto por punto
	T = Tnew.copy()

	T[N] = T[N-1]
	
	
	if n%20==0:
		plt.plot(np.arange(N+1)*deltax,T) #un plot un poco más discretizado para liberar memoria de python
		plt.pause(0.00001)
		plt.show()

plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('FTCS transporte')