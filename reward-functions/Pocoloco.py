def reward_function(params):

    #################################################################################
    '''
    Pocoloco reward function steps:

    1. Obtain track waypoints.
    2. Calculate optimal waypoints considering width of the track.
    3. Calculate maximum speed for next steps in the track.
    4. Calculate steering angle (left or right) based on waypoints ahead.
    5. Give more reward for a higher speed.
    '''

    import math

    # Read input variables
    center_waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    speed = params['speed']
    track_width = params['track_width']

    distance_from_center = params['distance_from_center']

    # Initialize the reward with typical value
    reward = 1.0

    # Calculate optimal waypoints
    

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])

    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)

    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    if reward == 1.0 and speed >= 1.75 and speed <= 4.0:
        reward += speed

    # Return reward as a float value
    return float(reward)
