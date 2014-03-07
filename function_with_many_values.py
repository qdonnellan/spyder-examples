import matplotlib.pyplot as plt
import numpy as np

def myfunc(x):
    return x**2

x = np.arange(0,10,0.5)

plt.plot(x,myfunc(x), 'o')
plt.show()

