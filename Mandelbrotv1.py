import sys
import matplotlib

import matplotlib.pyplot as plt
import numpy as np

from itertools import product

def iter_num(x, y, scale=100, max_n=50):
	n = 0
	z = 0
	c = x + 1j * y
	while n < max_n:
		z = z**2 + c
		n += 1
		if abs(z) >= 2:
			break
	if n == max_n:
		return x, y
	else:
		return 0, 0

scale = 1000
jana = np.linspace(-2, 2, num=scale)
koord = list(product(jana, jana))
mandelbrotX = []
mandelbrotY = []

for x in koord:
	a, b = iter_num(x[0], x[1], scale)
	mandelbrotX.append(a)
	mandelbrotY.append(b)



plt.scatter(mandelbrotX, mandelbrotY, s=0.5)
plt.grid()
plt.show()