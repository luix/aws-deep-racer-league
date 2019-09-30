import matplotlib.pyplot as plt
import numpy as np

#Shapely Library
from shapely.geometry import Point, Polygon
from shapely.geometry.polygon import LinearRing, LineString

# Track Name from Tracks List
# track_name = "New_York_Track"
track_name = "Mexico_track"

# Location of tracks folder
absolute_path = "."

# Get waypoints from numpy file
waypoints = np.load("%s/tracks-npy/%s.npy" % (absolute_path, track_name))
waypoints.shape

# Get number of waypoints
print("Number of waypoints[0] = " + str(waypoints.shape[0]))
print("Number of waypoints[1] = " + str(waypoints.shape[1]))
print("waypoints.shape = " + str(waypoints.shape))

l_center_line = LineString(waypoints[:,0:2])
l_inner_border = LineString(waypoints[:,2:4])
l_outer_border = LineString(waypoints[:,4:6])

# rescale waypoints to centimeter scale
center_line = waypoints[:,0:2] *100
inner_border = waypoints[:,2:4] *100
outer_border = waypoints[:,4:6] *100


# Plot waypoints
for i, point in enumerate(waypoints):
    # print("point.shape = " + str(point.shape))
    waypoint_center_line = (point[0], point[1]) * 10
    waypoint_inner_line = (point[2], point[3]) * 10
    waypoint_outer_line = (point[4], point[5]) * 10
    # plt.scatter(waypoint_outer_line[0], waypoint_outer_line[1])
    # plt.scatter(waypoint_center_line[0], waypoint_center_line[1])
    # plt.scatter(waypoint_inner_line[0], waypoint_inner_line[1])
    plt.scatter(waypoint_inner_line[0], waypoint_inner_line[1], color='green', marker='o', s=1, linewidths=0)
    plt.scatter(waypoint_center_line[0], waypoint_center_line[1], color='red', marker='o', s=1, linewidths=0)
    plt.scatter(waypoint_outer_line[0], waypoint_outer_line[1], color='blue', marker='o', s=1, linewidths=0)
    print("Waypoint " + str(i) + ": " + str(waypoint_center_line))

plt.show()
