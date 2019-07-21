###################
# Stay On Track
###################
#
# In this example, we give a high reward for when the car stays on the track,
# and penalize if the car deviates from the track boundaries.
#
# This example uses the all_wheels_on_track, distance_from_center and
# track_width parameters to determine whether the car is on the track,
# and give a high reward if so.
#
# Since this function doesn't reward any specific kind of behavior besides
# staying on the track, an agent trained with this function may take a longer
# time to converge to any particular behavior.

def reward_function(params):
    '''
    Example of rewarding the agent to stay inside the two borders of the track
    '''

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0

    # Always return a float value
    return float(reward)
