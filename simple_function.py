import matplotlib.pyplot as plt
import numpy as np

def myfunc(x):
    return 2*x

x = np.array([1,2,3,4,5,6,7,8,9,10])

plt.plot(x,myfunc(x), 'o')
plt.show()

