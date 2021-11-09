# Javier Mariño Villadamigo
import numpy as np
import matplotlib.pyplot as plt

r = 1.; k = 1.; P = 1e-5 # condiciones iniciales y definicion del paso de integracion
deltat = 0.1; t = 0
precminima = 1e-2; precmaxima = 1e-3 # rango en el que queremos que esté nuestro paso de integración

def f(P,t):
	f=r*P*(1-P/k)
	return f

plt.clf()
error = 0; listapuntoserror = [] # error es una variable "binaria" que nos dirá si hemos calculado puntos con un paso de integración fuera del intervalo (a veces nos veremos obligados a hacerlo para que este paso no diverja)
for i in range(1000):
	k1 = deltat*f(P,t)
	k2 = deltat*f(P+k1/2., t+deltat/2.)
	k3 = deltat*f(P+k2/2., t+deltat/2.)
	k4 = deltat*f(P+k3, t+deltat)

	Pnew = P + k1/6. + k2/3. + k3/3. + k4/6. # calculamos el primer Pnew con el que entrar al bucle (con RK4)

	while (np.abs(Pnew-P)>precminima or np.abs(Pnew-P)<precmaxima): # bucle que se ejecuta mientras el paso no esté en el intervalo
		deltatprevio = deltat # almacenamos el paso con el que entramos al bucle
		if np.abs(Pnew-P)>precminima:
			if deltat/1.1>0: # aunque a lo mejor no tenga mucho sentido, es posible que para un deltat suficientemente pequeño el ordenador lo trunque y sea 0
				deltat = deltat/1.1
			else:
				deltat=deltat
		elif np.abs(Pnew-P)<precmaxima:
			if deltat*1.1<1.: # con esto nos aseguramos de que no diverja
				deltat = deltat*1.1
			else:
				deltat=deltat

		k1 = deltat*f(P,t)
		k2 = deltat*f(P+k1/2., t+deltat/2.)
		k3 = deltat*f(P+k2/2., t+deltat/2.)
		k4 = deltat*f(P+k3, t+deltat)

		Pnew = P + k1/6. + k2/3. + k3/3. + k4/6.

		if deltatprevio == deltat and (np.abs(Pnew-P)>precminima or np.abs(Pnew-P)<precmaxima): # si hemos tenido que forzar a delta a permanecer entre 0 y 1 (i.e: deltatprevio = deltat) y el Pnew que hemos calculado no está lo suficientemente cerca de P, lo notificamos al usuario pero seguimos calculando aunque no sea la precisión deseada
			error +=1; listapuntoserror.append(t) # almacenamos los puntos que han sido calculados de esta forma
			break # salimos del while
			# esta sentencia se hace porque el paso tiene que estar confinado p.e. entre 0 y 1, de lo contrario método no calcula bien las trayectorias
	

		

	P = Pnew # ahora sí almacenamos el nuevo P
	t = t + deltat # y pasamos al siguiente

	plt.figure(2); plt.plot(t,deltat,'b.'); # evolucion del paso
	plt.figure(1); plt.plot(t,P,'r*')

if error > 0:
	print ('El método ha calculado %i puntos con una precisión indeseada. El tiempo en el que han sido tomados se ha almacenado en "listapuntoserror"' %(error))

plt.xlabel('t')
plt.ylabel('P')
plt.title('Logística por paso variable')
plt.xlim(0,25)
plt.show()