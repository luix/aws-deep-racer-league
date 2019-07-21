################
# No incentive
################
#
# An alternative strategy is to give a constant reward on each step,
# regardless of how the car is driving.
#
# This example doesn't use any of the input parameters — instead it returns
# a constant reward of 1.0 on each step.
#
# The agent's only incentive is to successfully finish the track, and it
# has no incentive to drive faster or follow any particular path. It may
# behave erratically.
#
# However, since the reward function doesn't constrain the agent's behavior,
# it may be able to explore unexpected strategies and behaviors that turn
# out to perform well.

def reward_function(params):
    '''
    Example of no incentive
    '''

    # Always return 1 if the car does not crash
    return 1.0
