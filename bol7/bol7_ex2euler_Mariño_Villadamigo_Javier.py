# autor: Javier Mariño Villadamigo
import numpy as np
import matplotlib.pyplot as plt

deltat=0.1
t=0
x=1
y=1
w0=1
w=1
b=0.5
F = 1
plt.clf()

def f(t,x,y):
	f=y
	return f
def g(t,x,y):
	g=F*np.cos(w*t)-w0**2*x-b*y
	return g


for i in range(500):
	xnew = x+deltat*f(t,x,y)
	ynew = y+deltat*g(t,x,y)
	x = xnew
	y = ynew
	t = t+deltat
	plt.plot(x,y,'r*')
	#plt.pause(0.0001) #para ver la evolución
plt.xlabel('x')
plt.ylabel('y')
plt.title('Oscilador amortiguado forzado Mét. Euler')
plt.show()
