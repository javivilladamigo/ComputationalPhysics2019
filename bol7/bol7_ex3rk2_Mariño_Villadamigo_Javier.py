import numpy as np
import matplotlib.pyplot as plt

deltat=0.01; t = 0; r = 1; k = 1; P = 10
plt.clf()

def f(P,t):
	f=r*P*(1-P/k)
	return f


for i in range(300):
	k1 = deltat*f(P,t)
	k2 = deltat*f(P+k1/2., t+deltat/2.)

	P = P+k2
	t=t+deltat
	plt.plot(t,P,'r*')

plt.xlabel('t')
plt.ylabel('P')
plt.title('Logística Runge-Kutta 2º orden')
plt.show()