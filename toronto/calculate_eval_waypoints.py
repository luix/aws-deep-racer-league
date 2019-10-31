import matplotlib.pyplot as plt
import numpy as np

# Shapely Library
from shapely.geometry import Point, Polygon
from shapely.geometry.polygon import LinearRing, LineString

# SciPy Interpolation https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
from scipy import interpolate

# Eval racing line control points
# racing_line_waypoints = [
#     [4.62055 , 1.61558], 
#     [3.03053 , 2.36438], 
#     [1.38568 , 2.22003], 
#     [1.04757 , 0.767549], 
#     [2.12586 , -0.423305], 
#     [5.01349 , -2.30882], 
#     [7.09697 , -1.56905], 
#     [7.04214 , 0.298425], 
#     [6.29282 , 0.975046], 
#     [4.62055 , 1.61558]]

# Training racing line control points
racing_line_waypoints = [
    [2.94664 , 2.25589],
    [1.09757 , 1.92673],
    [1.27275 , 0.866101],
    [2.44058 , -0.560263],
    [3.56948 , -1.98663],
    [5.63265 , -2.2975],
    [7.71529 , -2.7181], 
    [8.76633 , -1.96834], 
    [8.66902 , -0.871137], 
    [7.24815 , -0.176242],
    [6.31389 , 0.792954],
    [4.46482 , 1.74386],
    [2.94664 , 2.25589]] 

points = np.array(racing_line_waypoints)
x = points[:,0]
y = points[:,1] 

tck, u = interpolate.splprep([x, y], s=0)
unew = np.arange(0, 1.01, 0.01)
out = interpolate.splev(unew, tck)

plt.plot(x, y, 'x', out[0], out[1])

# for point in center_line_waypoints:
#     plt.scatter(point[0], point[1], c='w', marker='.', s=4, linewidths=0)

print('out[0].size', out[0].size)
print('out[0].shape', out[0].shape)
print('out[1].size', out[1].size)
print('out[1].shape', out[1].shape)

for i in range(101):
    print('[',out[0][i],',',out[1][i],'],')

plt.show()

