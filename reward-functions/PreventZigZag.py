#
# Prevent zig-zag
#
#
# This example incentivizes the agent to follow the center line but
# penalizes with lower reward if it steers too much, which will help
# prevent zig-zag behavior.
#
# The agent will learn to drive smoothly in the simulator and likely
# display the same behavior when deployed in the physical vehicle.

def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''

    # Read input params
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = params['steering']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the agent is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed or close to off track

    # Steering penality threshold. Note: change the number based on the action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_TRESHOLD:
        reward *= 0.8

    # Always return a float value
    return float(reward)
