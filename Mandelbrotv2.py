import sys
import matplotlib

import matplotlib.pyplot as plt
import numpy as np

from itertools import product

def iter_num(x, y, scale=600, max_n=100):
	n = 0
	z = 0
	xs = x/scale
	ys = y/scale
	c = xs + 1j * ys
	while n < max_n:
		z = z**2 + c
		n += 1
		if abs(z) >= 2:
			break
	if n == max_n:
		return xs, ys
	else:
		return 0, 0
	

scale = 600
coordinates = list(product(range(-2*scale, 2*scale),range(-2*scale, 2*scale)))
# print(coordinates)
# coordinatesNp = np.array(coordinates)

x, y = zip(*coordinates)

npIter = np.frompyfunc(iter_num, 2, 2)

mandelbrotX, mandelbrotY = npIter(list(x), list(y))

# print(list(mandelbrotX))
# print(list(mandelbrotY))

plt.scatter(mandelbrotX, mandelbrotY, s=0.5)
plt.grid()
plt.show()