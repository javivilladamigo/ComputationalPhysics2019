# Javier Mariño
import matplotlib.pyplot as plt
import numpy as np

dimt = 2500 # número de iteraciones temporales
deltat = 0.1; deltax = 0.5; alfa = 0.1; N = 20 # parámetros naturales de la discretización
s = alfa*deltat/deltax**2 # calculamos la estabilidad

# creo los dos vectores necesarios para calcular el tercero, el cual también inicializo
np.random.seed(30);
Told = np.zeros(N+1); Told[5:9]=5+5*np.random.sample(4)
Told[0]=0; Told[N]=10; T=Told.copy(); Tnew = T.copy()

plt.close('all')
plt.plot(np.arange(N+1)*deltax,Told,'-r'); plt.pause(0.00001)


for n in range(dimt):

	for i in range(1,N):
		Tnew[i]=(2/3)*s*(T[i+1]-2*T[i]+T[i-1])-1./3.*Told[i]+4./3.*T[i]
	Tnew[0]=0
	Tnew[N]=10
	
	if n%20==0:
		plt.plot(np.arange(N+1)*deltax,Tnew,'-'); plt.pause(0.00001)
		plt.show()
	Told = T.copy(); T=Tnew.copy()

plt.xlabel('$x$')
plt.ylabel('$T$')
plt.title('3 niveles temporales y centrado en el espacio')