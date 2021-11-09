# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

deltat=2.5
t=0
x=1
plt.clf()
for i in range(100):
	t=t+deltat
	x=x+deltat*np.sin(x)
	plt.plot(t,x,'r*')
	plt.show()
