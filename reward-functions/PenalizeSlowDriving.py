def reward_function(params):
        '''
        Example that penalizes slow driving. This create a non-linear reward
        function so it may take longer to learn.
        '''

        # Calculate 3 marks that are farther and farther away from the center line
        marker_1 = 0.1 * params['track_width']

        # Give higher reward if the car is closer to center line and vice versa
        if params['distance_from_center'] <= marker_1:
                reward = 1
        elif params['distance_from_center'] <= marker_2:
                reward = 0.5
        elif params['distance_from_center'] <= marker_3:
                reward = 0.1
        else:
                reward = 1e-3   # likely crashed/ close to off track

        # penalize reward for the car taking slow actions
        # speed in m/s
        # the below assumes your action space has a maximum speed of 5 m/s
        # and speed granularity of 3
        # we penalize any speed less than 2m/s
        SPEED_THRESHOLD = 2
        if params['speed'] < SPEED_THRESHOLD:
                reward *= 0.5

        return float(reward)
