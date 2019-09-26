import matplotlib.pyplot as plt
import numpy as np

# Track Name from Tracks List
# track_name = "New_York_Track"
track_name = "Mexico_track"

# Location of tracks folder
absolute_path = "."

# Get waypoints from numpy file
waypoints = np.load("%s/tracks-npy/%s.npy" % (absolute_path, track_name))

# Get number of waypoints
print("Number of waypoints = " + str(waypoints.shape[0]))

# Plot waypoints
for i, point in enumerate(waypoints):
    waypoint = (point[2], point[3])
    plt.scatter(waypoint[0], waypoint[1])
    print("Waypoint " + str(i) + ": " + str(waypoint))

plt.show
