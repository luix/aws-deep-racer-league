# Empire-City-Training-model-July-2019

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    import math

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

    # Penalize if car is very near to exit the tracj=k
    if distance_from_center >= (0.9*track_width/2) :
        return float(-100)
    # Reward if car is within the track
    else:
        reward = 10

    # Reward according to speed
    reward += speed * 100.0

    # Reward according to progress
    reward += progress * 2.0

    # Reward according to steps
    reward += steps * 2.0

    # Reward according to less steering
    reward += ( 50 - steering_angle )

    # Reward if car is closer to way_points

    return float(reward)
