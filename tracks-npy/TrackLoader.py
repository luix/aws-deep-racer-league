import numpy as np

#img_array = np.load('Virtual_May19_Train_track.npy')
img_array = np.load('London_Loop_Train.npy')

from matplotlib import pyplot as plt

plt.imshow(img_array)
plt.show()
