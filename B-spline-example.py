import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sps
import scipy.interpolate as spi

# plot cubic cardinal B-spline (knots 0, 1, 2, 3, 4)
p = 3
xx = np.linspace(0, p+1, 100)
yy = sps.bspline(xx - (p+1)/2, p)
plt.plot(xx, yy)
plt.show()

# plot cubic non-uniform spline (m=5 DOFs)
xi = [0, 1, 3, 4, 6, 7, 8, 10, 11]
c = [2, -1, 1, 0, 1]
s = spi.BSpline(xi, c, p)
m = len(c)
xx = np.linspace(xi[p], xi[m])
yy = s(xx)
plt.plot(xx, yy)
plt.show()
