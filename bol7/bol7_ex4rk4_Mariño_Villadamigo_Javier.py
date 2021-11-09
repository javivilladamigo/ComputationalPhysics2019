# Javier Mariño Villadamigo
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




sigma = 3; r = 26.5; b = 1
#sigma = 10.5; r = 33.5; b = 1.8
deltat = 0.01; t = 0
x = 0.01; y = 1; z = 0

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

	k1x = deltat*dx(x,y,z,t)
	k1y = deltat*dy(x,y,z,t)
	k1z = deltat*dz(x,y,z,t)

	k2x = deltat*dx(x+k1x/2., y+k1y/2., z+k1z/2., t+deltat/2.)
	k2y = deltat*dy(x+k1x/2., y+k1y/2., z+k1z/2., t+deltat/2.)
	k2z = deltat*dz(x+k1x/2., y+k1y/2., z+k1z/2., t+deltat/2.)

	k3x = deltat*dx(x+k2x/2., y+k2y/2., z+k2z/2., t+deltat/2.)
	k3y = deltat*dy(x+k2x/2., y+k2y/2., z+k2z/2., t+deltat/2.)
	k3z = deltat*dz(x+k2x/2., y+k2y/2., z+k2z/2., t+deltat/2.)

	k4x = deltat*dx(x+k3x, y+k3y, z+k3z, t+deltat)
	k4y = deltat * dy(x+k3x,y+k3y, z+k3z, t+deltat)
	k4z = deltat*dz(x+k3x, y+k3y, z+k3z, t+deltat)


	x = x + k1x/6. + k2x/3. + k3x/3. + k4x/6.
	y = y + k1y/6. + k2y/3. + k3y/3. + k4y/6.
	z = z + k1z/6. + k2z/3. + k3z/3. + k4z/6.
	X.append(x); Y.append(y); Z.append(z)
	t = t+deltat

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(X,Y,Z, 'b-')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
plt.title('Atractor de Lorenz Runge-Kutta 4º orden')
plt.show()


