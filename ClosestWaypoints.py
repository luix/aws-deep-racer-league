def reward_function(params):

    #################################################################################
    '''
    Example of using waypoints and heading to make the car run in the right direction
    '''

    import math

    # Read input variables
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
