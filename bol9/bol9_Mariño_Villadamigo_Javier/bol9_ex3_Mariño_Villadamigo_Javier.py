# Javier Mariño
## DUFORT FRANKEL conveccion ##
import matplotlib.pyplot as plt
import numpy as np


dimt = 1000 # número de iteraciones temporales
deltat = 0.1; deltax = 0.5; C = 0.1; u =C*deltax/deltat

N = 200 # parámetros naturales de la discretización


T = np.zeros(N+1)
#np.random.seed(8); 
#T[6:10]=2.5+5*np.random.sample(4);
T[6:10]=5
Told = T.copy(); Tnew = T.copy()

plt.close('all')
plt.plot(np.arange(N+1)*deltax,Told,'-r'); plt.pause(0.00001)

for n in range(dimt):

	for i in range(1,N):
		Tnew[i]=Told[i]-C*(T[i+1]-T[i-1])

	Tnew[N]=Tnew[N-1]


	if n%10==0:
		plt.plot(np.arange(N+1)*deltax,Tnew,'-'); plt.pause(0.00001)
		plt.show()
	Told=T.copy(); T=Tnew.copy()

plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('Dufort-Frankel')