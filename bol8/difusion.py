import matplotlib.pyplot as plt
import numpy as np

N = 20; dimt = 1000
deltat = 0.1; deltax = 0.5; alfa = 1

T = np.zeros(N+1)
T[0]=100

Tnew = np.zeros(N+1)
plt.close('all')
plt.plot(T,'-r'); plt.pause(0.1)

for n in range(dimt):
	for i in range(1,N):
		T[i] = T[i]+alfa*deltat/deltax**2*(T[i+1]-2.*T[i]+T[i-1])
	T[0]=100
	T[N]=0
	if n%10==0:
		plt.plot(T)
		plt.pause(0.5)
		plt.show()
plt.xlabel('i-indice')
plt.ylabel('Temperatura')