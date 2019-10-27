import numpy as np
from scipy.spatial import distance
from sklearn.metrics.pairwise import euclidean_distances
import math

# 1
def eudis1(v1, v2):
    return np.linalg.norm(v1-v2)

# 2
def eudis2(v1, v2):
    return distance.euclidean(v1, v2)

# 3
def eudis3(v1, v2):
    return euclidean_distances(v1, v2)

# 5
def eudis5(v1, v2):
    dist = [(a - b)**2 for a, b in zip(v1, v2)]
    dist = math.sqrt(sum(dist))
    return dist

dis1 = (52, 106, 35, 12)
dis2 = (33, 153, 75, 10)
v1, v2 = np.array(dis1), np.array(dis2)

import timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

wrappered1 = wrapper(eudis1, v1, v2)
wrappered2 = wrapper(eudis2, v1, v2)
wrappered3 = wrapper(eudis3, v1, v2)
wrappered5 = wrapper(eudis5, v1, v2)
t1 = timeit.repeat(wrappered1, repeat=3, number=100000)
t2 = timeit.repeat(wrappered2, repeat=3, number=100000)
t3 = timeit.repeat(wrappered3, repeat=3, number=100000)
t5 = timeit.repeat(wrappered5, repeat=3, number=100000)

print('\n')
print('t1: ', sum(t1)/len(t1))
print('t2: ', sum(t2)/len(t2))
print('t3: ', sum(t3)/len(t3))
print('t5: ', sum(t5)/len(t5))

