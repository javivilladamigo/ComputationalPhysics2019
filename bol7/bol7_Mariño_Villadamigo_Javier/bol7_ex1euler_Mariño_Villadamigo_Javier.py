# autor: Javier Mariño Villadamigo
import numpy as np
import matplotlib.pyplot as plt

deltat=0.1
t=0
x=1
y=1
w0=1
plt.clf()

for i in range(100):
	xnew = x+deltat*y
	ynew = y+deltat*(-w0**2*x)
	x = xnew
	y = ynew
	t = t+deltat
	plt.plot(x,y,'r*')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Oscilador armónico Mét. Euler')
plt.show()