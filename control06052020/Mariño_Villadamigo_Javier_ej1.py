# autor: Javier Mariño Villadamigo
import numpy as np
import matplotlib.pyplot as plt

deltat=0.01
a = 1.; b = 3.; t = 0
# ci
u = 0.3; v = 0.5

plt.clf()

def du(t,u,v): # dx/dt = f
	du = a+ u**2*v-b*u-u
	return du
def dv(t,u,v): # dy/dt = g
	dv = b*u-u**2*v
	return dv


for n in range(5000):
	
	k1u = deltat*du(u,v,t)
	k1v = deltat*dv(u,v,t)
	k2u =deltat*du(t+deltat/2.,u+k1u/2.,v+k1v/2.)
	k2v = deltat*dv(t+deltat/2.,u+k1u/2.,v+k1v/2.)
	k3u = deltat*du(t+deltat/2.,u+k2u/2.,v+k2v/2.)
	k3v = deltat*dv(t+deltat/2.,u+k2u/2.,v+k2v/2.)
	k4u = deltat*du(t+deltat, u+k3u, v+k3v)
	k4v = deltat * dv(t+deltat,u+k3u,v+k3v)
	unew = u + k1u/6. + k2u/3. + k3u/3. + k4u/6.
	vnew = v + k1v/6. + k2v/3. + k3v/3. + k4v/6.
	u=unew
	v=vnew
	t = t+deltat
	if n%50==0:
		plt.plot(u,v,'r*'); plt.pause(0.000000001)
		plt.show()
	

plt.xlabel('u')
plt.ylabel('v')
plt.title('Brusselator')


