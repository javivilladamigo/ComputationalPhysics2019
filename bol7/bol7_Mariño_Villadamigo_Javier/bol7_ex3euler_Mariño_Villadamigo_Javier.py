# Javier Mariño Villadamigo
import numpy as np
import matplotlib.pyplot as plt

r = 1.; k = 1.; P = 0.01
deltat = 0.01; t = 0

def f(P,t):
	f=r*P*(1-P/k)
	return f

plt.clf()

for i in range(1000):
	P = P + deltat*f(P,t)
	plt.plot(t,P,'r*')
	t = t+deltat
plt.xlabel('t')
plt.ylabel('P')
plt.title('Logística Mét. Euler')
plt.show()