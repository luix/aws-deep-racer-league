def reward_function(params):

    import math
    import json
    print(json.dumps(params))

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']

    reward = 1e-3

    # Reward if car stays on the track and get around in as few steps as possible
    if distance_from_center < ( track_width/2*0.92 ) and progress > 0:
        reward = (progress * 100) + (speed**2)

    return float(reward)
