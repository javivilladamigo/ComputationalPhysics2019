
import numpy as np
import matplotlib.pyplot as plt

deltat=0.01; t = 0; r = 1.; k = 1; P = 10
plt.clf()



def f(P,t):
	f=r*P*(1-P/k)
	return f



for i in range(300):
	
	k1 = deltat*f(P,t)
	k2 =deltat*f(P+k1/2., t+deltat/2.)
	k3 = deltat*f(P+k2/2., t+deltat/2.)
	k4 = deltat*f(P+k3,t+deltat)

	P = P + k1/6. + k2/3. + k3/3. + k4/6.
	t = t+deltat

	plt.plot(t,P,'r*')
plt.xlabel('t')
plt.ylabel('P')
plt.title('Logística Runge-Kutta 4º orden')
plt.show()