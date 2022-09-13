import sys
import matplotlib

import matplotlib.pyplot as plt
import numpy as np

def iter_num(c, max_n=100):
    n = 0
    z = 0
    while n < max_n:
        z = z**2 + c
        n += 1
        if abs(z) > 2:
            break
    return n

desimaali = 400
pituus = 2*desimaali

koordx = []
koordy = []

for x in range(-pituus,pituus):
    for y in range(-pituus,pituus):
        c = x/desimaali + 1j * y/desimaali
        n = iter_num(c)
        if n == 100:
            koordx.append(x/desimaali)
            koordy.append(y/desimaali)


x = np.array(koordx)
y = np.array(koordy)

plt.scatter(x, y, s = 0.1)
plt.grid()
plt.show()


# Muista komento: pip install matplotlib ladataksesi tarvittava kirjasto