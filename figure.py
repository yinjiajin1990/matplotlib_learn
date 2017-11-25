import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = x**2
y2 = x*2

plt.figure()
plt.plot(x,y1,label='up')
plt.plot(x,y2,color='red',linestyle='--',label='down')
plt.xlabel("x name")
plt.ylabel("y name")
plt.yticks([1],['good'])
plt.legend()

plt.show()