def reward_function(params):

    import math
    import json
    print(json.dumps(params))

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])
    closest_waypoints = params['closest_waypoints']
    is_left_of_center = params['is_left_of_center']

    next_point = closest_waypoints[1]

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if (0.5*track_width - distance_from_center) >= 0.05:
        reward = 10.0

    if speed >= 1.75 and speed <= 5.0:
        reward += speed

    if steering_angle < 15:
        reward += ( 15 - steering_angle)

    # Always return a float value
    return float(reward)
