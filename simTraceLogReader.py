'''
Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import gzip
import glob
import math
from datetime import datetime

EPISODE_PER_ITER = 20

def load_data(fname):
    data = []
    with open(fname, 'r') as f:
        for line in f.readlines():
            if "SIM_TRACE_LOG" in line:
                parts = line.split("SIM_TRACE_LOG:")[1].split('\t')[0].split(",")
                data.append(",".join(parts))
    return data

def convert_to_pandas(data, wpts=None):

    """
    stdout_ = 'SIM_TRACE_LOG:%d,%d,%.4f,%.4f,%.4f,%.2f,%.2f,%d,%.4f,%s,%s,%.4f,%d,%.2f,%s\n' % (
            self.episodes, self.steps, model_location[0], model_location[1], model_heading,
            self.steering_angle,
            self.speed,
            self.action_taken,
            self.reward,
            self.done,
            all_wheels_on_track,
            current_progress,
            closest_waypoint_index,
            self.track_length,
            time.time())
        print(stdout_)
    """

    df_list = list()

    #ignore the first two dummy values that coach throws at the start.
    for d in data[2:]:
        parts = d.rstrip().split(",")
        episode = int(parts[0])
        steps = int(parts[1])
        x = 100*float(parts[2])
        y = 100*float(parts[3])
        ##cWp = get_closest_waypoint(x, y, wpts)
        yaw = float(parts[4])
        steer = float(parts[5])
        throttle = float(parts[6])
        action = float(parts[7])
        reward = float(parts[8])
        done = 0 if 'False' in parts[9] else 1
        all_wheels_on_track = parts[10]
        progress = float(parts[11])
        closest_waypoint = int(parts[12])
        track_len = float(parts[13])
        tstamp = parts[14]

        #desired_action = int(parts[10])
        #on_track = 0 if 'False' in parts[12] else 1

        iteration = int(episode / EPISODE_PER_ITER) +1
        df_list.append((iteration, episode, steps, x, y, yaw, steer, throttle, action, reward, done, all_wheels_on_track, progress,
                        closest_waypoint, track_len, tstamp))

    header = ['iteration', 'episode', 'steps', 'x', 'y', 'yaw', 'steer', 'throttle', 'action', 'reward', 'done', 'on_track', 'progress', 'closest_waypoint', 'track_len', 'timestamp']

    df = pd.DataFrame(df_list, columns=header)
    return df


stream_name = '0'
fname = 'shanghai-sudu-training/simulation-logs/sim-trace-log-%s.log' %stream_name
#download_log(fname, stream_prefix=stream_name)
data = load_data(fname)
df = convert_to_pandas(data, None)
print("shape = ", df.shape)
print("size = ", df.size)
df.plot(kind='line', x='x', y='y', color='red')
plt.show()
# export = 'export-%s.xlsx' %stream_name
# df.to_excel(export)
