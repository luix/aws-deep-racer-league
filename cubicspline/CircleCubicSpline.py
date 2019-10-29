from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np 

theta = 2 * np.pi * np.linspace(0, 1, 5)

y = np.c_[np.cos(theta), np.sin(theta)]
cs = CubicSpline(theta, y, bc_type='periodic')

print("ds/dx={:.1f} ds/dy={:.1f}".format(cs(0, 1)[0], cs(0, 1)[1]))

xs = 2 * np.pi * np.linspace(0, 1, 100)

fig, ax = plt.subplots(figsize=(6.5, 4))

ax.plot(y[:, 0], y[:, 1], 'o', label='data')
ax.plot(np.cos(xs), np.sin(xs), label='true')
ax.plot(cs(xs)[:, 0], cs(xs)[:, 1], label='spline')
ax.axes.set_aspect('equal')
ax.legend(loc='center')

plt.show()