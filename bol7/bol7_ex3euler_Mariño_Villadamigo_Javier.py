import numpy as np
import matplotlib.pyplot as plt

r = 1.; k = 1.; P = 10
deltat = 0.01; t = 0

def f(P,t):
	f=r*P*(1-P/k)
	return f

plt.clf()

for i in range(300):
	P = P + deltat*f(P,t)
	t = t+deltat
	plt.plot(t,P,'r*')
plt.xlabel('t')
plt.ylabel('P')
plt.title('Logística Mét. Euler')
plt.show()