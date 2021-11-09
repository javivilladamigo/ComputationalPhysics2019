# Javier Mariño
import matplotlib.pyplot as plt
import numpy as np


dimt = 2500 # número de iteraciones temporales
deltat = 0.1; deltax = 0.5; alfa = 0.1; N = 20 # parámetros naturales de la discretización
s = alfa*deltat/deltax**2 # calculamos la estabilidad


T = np.zeros(N+1)
#np.random.seed(8); 
T[6:10]=2.5+5*np.random.sample(4); T[0]=0; T[N]=10
Told = T.copy(); Tnew = T.copy()

plt.close('all')
plt.plot(np.arange(N+1)*deltax,Told,'-r'); plt.pause(0.00001)

for n in range(dimt):

	for i in range(1,N):
		Tnew[i]=2*s/(1+2*s)*(T[i-1]+T[i+1])+(1-2*s)/(1+2*s)*Told[i]
	Tnew[0]=0
	Tnew[N]=10

	if n%20==0:
		plt.plot(np.arange(N+1)*deltax,Tnew,'-'); plt.pause(0.00001)
		plt.show()
	Told=T.copy(); T=Tnew.copy()

plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('Dufort-Frankel')