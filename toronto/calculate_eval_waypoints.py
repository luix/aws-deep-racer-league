import matplotlib.pyplot as plt
import numpy as np

# Shapely Library
from shapely.geometry import Point, Polygon
from shapely.geometry.polygon import LinearRing, LineString

# SciPy Interpolation https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
from scipy import interpolate


racing_line_waypoints = [
    [2.0, 0.0],
    [4.0, 2.0],
    [6.0, 0.0],
    [4.0, -2.0],
    [2.0, 0.0]]
    # [3.02972, 2.39258],
    # [1.37140, 2.19255],
    # [1.02819, 0.811976],
    # [2.17091, -0.407792],
    # [3.34307, -1.66041],
    # [5.00628, -2.29431],
    # [6.87052, -2.74535],
    # [8.63335, -1.91387],
    # [8.43055, -0.556831],
    # [7.82420, -0.282285],
    # [6.77468, 0.192287],
    # [4.49962, 1.66699],
    # #[6.64431, 0.588418],
    # [3.02972, 2.39258]]
    # #[3.09133, 2.31021]]

points = np.array(racing_line_waypoints)
x = points[:,0]
y = points[:,1] 

tck, u = interpolate.splprep([x, y], s=0)
unew = np.arange(0, 1.01, 0.01)
out = interpolate.splev(unew, tck)

plt.plot(x, y, 'x', out[0], out[1])

# for point in center_line_waypoints:
#     plt.scatter(point[0], point[1], c='w', marker='.', s=4, linewidths=0)

plt.show()

