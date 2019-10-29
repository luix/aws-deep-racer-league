from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np 

y = [-1.0, 0.0, 1.0, 0.0]
x = [0.0, 1.0, 0.0, -1.0]

cs = CubicSpline(x, y, bc_type='periodic')

fig, ax = plt.subplots(figsize=(6.5, 4))

ax.plot(cs(xs)[:, 0], cs(xs)[:, 1], label='spline')

plt.show()