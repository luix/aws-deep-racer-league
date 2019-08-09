
import matplotlib.pyplot as plt

params = {
  'all_wheels_on_track': True,
  'x': 4,
  'y': 5,
  'distance_from_center': 0.3,
  'heading': 359.9,
  'progress': 50,
  'steps': 100,
  'speed': 1.0,
  'steering_angle': 6,
  'track_width': 0.2,
  'waypoints': [[ 2.5, 0.75], [3.33, 0.75], [4.17, 0.75], [5.0, 0.75], [5.83, 0.75], [6.67, 0.75], [7.5, 0.75], [8.33, 0.75], [9.17, 0.75], [9.75, 0.94], [10.0, 1.5], [10.0, 1.875], [9.92, 2.125], [9.58, 2.375], [9.17, 2.75], [8.33, 2.5], [7.5, 2.5], [7.08, 2.56], [6.67, 2.625], [5.83, 3.44], [5.0, 4.375], [4.67, 4.69], [4.33, 4.875], [4.0, 5.0], [3.33, 5.0], [2.5, 4.95], [2.08, 4.94], [1.67, 4.875], [1.33, 4.69], [0.92, 4.06], [1.17, 3.185], [1.5, 1.94], [1.6, 1.5], [1.83, 1.125], [2.17, 0.885 ]],
  'closest_waypoints': [3, 4],
  'is_left_of_center': True,
  'is_reversed': True
}

# The Official re:Invent 2019 League Summit Circuit track waypoints
waypoints = [[ 2.5, 0.75], [3.33, 0.75], [4.17, 0.75], [5.0, 0.75], [5.83, 0.75], [6.67, 0.75], [7.5, 0.75], [8.33, 0.75], [9.17, 0.75], [9.75, 0.94], [10.0, 1.5], [10.0, 1.875], [9.92, 2.125], [9.58, 2.375], [9.17, 2.75], [8.33, 2.5], [7.5, 2.5], [7.08, 2.56], [6.67, 2.625], [5.83, 3.44], [5.0, 4.375], [4.67, 4.69], [4.33, 4.875], [4.0, 5.0], [3.33, 5.0], [2.5, 4.95], [2.08, 4.94], [1.67, 4.875], [1.33, 4.69], [0.92, 4.06], [1.17, 3.185], [1.5, 1.94], [1.6, 1.5], [1.83, 1.125], [2.17, 0.885 ]]

import math

track_lenght = 0
prev_x = 4.297569990158081
prev_y = 0.5397330448031425
print(track_lenght)
num = 0
for point in waypoints:
    plt.annotate(num, (point[0], point[1]), size=7)
    plt.scatter(point[0], point[1], marker='o', s=5, linewidths=0)
    num+=1
    track_lenght += math.sqrt((point[0]-prev_x)**2 + (point[1]-prev_y)**2)
    prev_x = point[0]
    prev_y = point[1]
    print(track_lenght)
    #plt.scatter(point[0], point[1] - 0.33, c='r', marker='o', s=1, linewidths=0)
    #plt.scatter(point[0], point[1] + 0.33, c='b', marker='o', s=1, linewidths=0)

plt.grid(True)
plt.tight_layout()
plt.show()
