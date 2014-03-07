import matplotlib.pyplot as plt
import numpy as np

def firstfunc(x):
    return x**2

def secondfunc(x):
    return x**3

x = np.arange(0,10,0.1)

plt.xlabel('This is the horizontal axis')
plt.ylabel('This is the vertical axis')
plt.title('This is a very good title')

plt.plot(x,firstfunc(x), 'o')
plt.plot(x,secondfunc(x), 'r-')
plt.show()

