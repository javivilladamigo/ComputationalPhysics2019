import numpy as np
import matplotlib.pyplot as plt

deltat=0.1
t=0
x=1
plt.clf()
for i in range(100):
	t=t+deltat
	k1=deltat*np.sin(x)
	k2=deltat*np.sin(x+k1/2.)
	x=x+k2
	plt.plot(t,x,'r*')
	plt.xlabel('t')
	plt.ylabel('x')

plt.xlim(0,10)
plt.ylim(0,4)
plt.show()