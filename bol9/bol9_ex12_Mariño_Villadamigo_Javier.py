# Javier Mariño
## DIFUSION BIDIMENSIONAL FTCS ##
import matplotlib.pyplot as plt
import numpy as np

plt.ion()

dimt = 500; deltat = 0.1; N = 50 # parámetros naturales de la discretización
deltax = 0.5; alphax = 0.5; sx = alphax*deltat/deltax**2
deltay = 0.5; alphay = 0.5; sy = alphay*deltat/deltay**2


T = np.zeros((N+1, N+1));
Tnew = T.copy()
'''
for i in range(1,N):
	for j in range(1,N):
		if i == j :
			T[i,j] = 10
'''

T[20:30,20:30] = 10



plt.close('all')
plt.imshow(T, cmap='hot')
plt.colorbar()
plt.pause(0.1)
plt.show()


for n in range(dimt):
	for i in range(1,N):
		for j in range(1,N):
			Tnew[i,j] = T[i,j] + sx*(T[i-1,j]-2*T[i,j]+T[i+1,j])+sy*(T[i,j-1]-2*T[i,j]+T[i,j+1])
	T = Tnew.copy();

	# cc
	T[0,:] = T[1,:]
	T[N,:] = T[N-1,:]
	T[:,0] = T[:,1]
	T[:,N] = T[:,N-1]

	if n%50==0:
		plt.imshow(T, cmap='hot')
		plt.pause(0.00000000001)
		plt.show()


		




