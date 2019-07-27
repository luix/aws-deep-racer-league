def reward_function(params):

    import math
    import json
    print(json.dumps(params))

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    waypoints = params['waypoints']
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress']
    steps = params['steps']
    steering_angle = abs(params['steering_angle'])

    reward = 1e-3

    # Reward if car stays on the track and get around in as few steps as possible
    if distance_from_center < ( track_width/2*0.92 ) and progress > 0:
        reward = (progress * 100) + (speed**2)
    else:
        print("reward: {0}".format(reward))
        return float(reward)

    # Reward according to speed
    reward += speed * 10.0

    # Reward according to progress
    reward += progress * 2.0

    # Reward according to steps
    # reward += steps

    # Reward according to less steering
    reward += ( 50 - steering_angle )

    print("reward: {0}".format(reward))

    return float(reward)
