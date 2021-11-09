# Javier Mariño
## DUFORT-FRANKEL TRANSPORTE ##
import matplotlib.pyplot as plt
import numpy as np

dimt = 1000 # número de iteraciones temporales
deltat = 0.1; deltax = 0.5; 
C = 0.5; alpha = 1.0
u = C*deltax/deltat 
s = alpha*deltat/deltax**2
N = 200 # parámetros naturales de la discretización

T = np.zeros(N+1); T[5:30]=np.ones(25)*1; #T[N]=10 # vector inicial, con las c.i. que queramos
Tnew = T.copy(); Told = T.copy()

plt.close('all')
plt.plot(np.arange(N+1)*deltax,T,'-r'); plt.pause(0.00001) # primera representacion

for n in range(dimt):
	for i in range(1,N):
		Tnew[i]=(1/(1+2*s))*(Told[i]-C*(T[i+1]-T[i-1])+(2*s)*(T[i-1]-Told[i]+T[i+1]))
	Tnew=(Tnew+T)/2

	T = Tnew.copy(); Told = T.copy()
	
	T[N]=T[N-1]
	
	if n%10==0:
		plt.plot(np.arange(N+1)*deltax, T) #un plot un poco más discretizado para liberar memoria de python
		plt.pause(0.0000001)
		plt.show()

plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('dufort-frankel transporte')