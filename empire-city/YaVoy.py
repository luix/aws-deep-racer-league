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

    reward = 1e-3

    if next_point >= 0 and next_point <= 17 and speed >= 2.25 and speed <= 4.0 and not is_left_of_center:
        reward = 10

    elif next_point >= 21 and next_point <= 28 and speed >= 1.75 and speed <= 3.0 and is_left_of_center:
        reward = 10

    elif next_point >= 31 and next_point <= 41 and speed >= 2.25 and speed <= 4.0 and not is_left_of_center:
        reward = 10

    elif next_point >= 45 and next_point <= 58 and speed >= 1.75 and speed <= 3.0 and is_left_of_center:
        reward = 10

    elif next_point >= 65 and next_point <= 75 and speed >= 2.25 and speed <= 4.0 and not is_left_of_center:
        reward = 10

    elif next_point >= 86 and next_point <= 104 and speed >= 2.25 and speed <= 4.0 and not is_left_of_center:
        reward = 10

    elif next_point >= 110 and next_point <= 125 and speed >= 1.75 and speed <= 3.0 and is_left_of_center:
        reward = 10

    elif next_point >= 135 and next_point <= 144 and speed >= 1.75 and speed <= 3.0 and not is_left_of_center:
        reward = 10

    elif next_point >= 150 and next_point <= 163 and speed >= 1.75 and speed <= 3.0 and is_left_of_center:
        reward = 10

    elif next_point >= 165 and next_point <= 171 and speed >= 2.25 and speed <= 4.0 and not is_left_of_center:
        reward = 10

    print("reward: {0}".format(reward))

    return float(reward)
