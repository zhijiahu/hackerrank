
from random import uniform
import matplotlib.pyplot as plt
import numpy as np

def approx(pts):
    count = 0
    in_quatrant = []

    for p in pts:
        if (p[0] ** 2 + p[1] ** 2) <= 1:
            count += 1
            in_quatrant.append(p)

    return (count / len(pts) * 4, in_quatrant)

num = 1000
pts = [[uniform(0,1), uniform(0,1)] for _ in range(num)]

pi, hits = approx(pts)
print('Approx of pi = {}'.format(pi))

p = np.array(pts)
h = np.array(hits)
plt.scatter(p[:,0], p[:,1])
plt.scatter(h[:,0], h[:,1], c='red')
plt.show()
