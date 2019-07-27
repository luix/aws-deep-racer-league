######################
# Follow Center Line
######################
#
# In this example we measure how far away the car is from the center
# of the track, and give a higher reward if the car is close to the center line.
#
# This example uses the track_width and distance_from_center parameters,
# and returns a decreasing reward the further the car is from the center of the
# track.
#
# This example is more specific about what kind of driving behavior to reward,
# so an agent trained with this function is likely to learn to follow the track
# very well. However, it is unlikely to learn any other behavior such as
# accelerating or braking for corners.

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Calculate 3 markers that are at varying distances away from center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give hi
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_frame_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed or close to off track

    # Always return a float value
    return float(reward)
