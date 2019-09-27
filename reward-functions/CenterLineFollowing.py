def reward_function(params)"
        '''
        Example of rewarding the agent to follow center line
        '''

        # Calculate 3 marks that are farther and farther away from the center line
        marker_1 = 0.1 * params['track_width']
        marker_2 = 0.25 * params['track_width']
        marker_3 = 0.5 * params['track_width']

        # Give higher reward if the car is closer to center line and vice versa
        if params['distance_from_center'] <= marker_1:
                reward = 1.0
        elif params['distance_from_center'] <= marker_2:
                reward = 0.5
        elif params['distance_from_center'] <= marker_3:
                reward = 0.1
        else:
                reward = 1e-3   # likely crashed / close to off track

        return float(reward)
