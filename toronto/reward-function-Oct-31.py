def reward_function(params):
    '''
    This was the reward function used in the model submission on Thursday, October 31st

    Lap time was 18.497 secs

    ~~ Rest In Peace ~~

    '''
    
    # Read input parameters
    speed = params['speed']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    
    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward += 10.0
    elif distance_from_center <= marker_2:
        reward += 5.0
    elif distance_from_center <= marker_3:
        reward += 1.0
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    if reward >= 0.5:
        if speed >= 2.7:
            reward += speed
        reward += (progress/10)

    return float(reward)