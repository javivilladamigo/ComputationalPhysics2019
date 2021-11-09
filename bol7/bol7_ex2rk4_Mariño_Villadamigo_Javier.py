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

def f(t,x,y): # dx/dt = f
	f=y
	return f
def g(t,x,y): # dy/dt = g
	g = F*np.cos(w*t)-w0**2*x-b*y
	return g


for i in range(500):
	
	k1x = deltat*f(t,x,y)
	k1y = deltat*g(t,x,y)
	k2x =deltat*f(t+deltat/2.,x+k1x/2.,y+k1y/2.)
	k2y = deltat*g(t+deltat/2.,x+k1x/2.,y+k1y/2.)
	k3x = deltat*f(t+deltat/2.,x+k2x/2.,y+k2y/2.)
	k3y = deltat*g(t+deltat/2.,x+k2x/2.,y+k2y/2.)
	k4x = deltat*f(t+deltat, x+k3x, y+k3y)
	k4y = deltat * g(t+deltat,x+k3x,y+k3y)
	xnew = x + k1x/6. + k2x/3. + k3x/3. + k4x/6.
	ynew = y + k1y/6. + k2y/3. + k3y/3. + k4y/6.
	x=xnew
	y=ynew
	t = t+deltat

	plt.plot(x,y,'r*')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Oscilador amortiguado forzado Runge-Kutta 4º orden')

plt.show()


