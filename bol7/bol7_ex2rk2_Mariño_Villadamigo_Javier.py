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
	
	k1x = deltat*f(t,x,y)
	k1y = deltat*g(t,x,y)
	k2x = deltat*f(t+deltat/2., x+k1x/2., y+k1y/2.)
	k2y = deltat*g(t+deltat/2., x+k1x/2., y+k1y/2.)

	x = x+k2x
	y = y+k2y


	t=t+deltat

	

	plt.plot(x,y,'r*')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Oscilador amortiguado forzado Runge-Kutta 2º orden')
plt.show()