# Javier Mariño Villadamigo
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


sigma = 3; r = 26.5; b = 1
deltat = 0.01; t = 0
x = 0; y = 1; z = 0

def dx(x,y,z,t):
	dx = sigma*(y-x)
	return dx


def dy(x,y,z,t):
	dy = r*x-y-x*z
	return dy

def dz(x,y,z,t):
	dz = x*y-b*z
	return dz

X=[]; Y=[]; Z=[]
for i in range(5000):
	xnew = x + deltat*dx(x,y,z,t)
	ynew = y + deltat*dy(x,y,z,t)
	znew = z + deltat*dz(x,y,z,t)
	x = xnew; y = ynew; z = znew

	t = t+deltat
	X.append(x); Y.append(y); Z.append(z)
	
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(X,Y,Z, 'b-')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
plt.title('Atractor de Lorenz Mét. Euler')
plt.show()