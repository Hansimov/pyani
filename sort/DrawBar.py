import numpy as np
import matplotlib.pyplot as plt
from random import shuffle
from matplotlib.animation import FuncAnimation
from time import sleep

arrayLength = 100
xValues = np.arange(1, arrayLength + 1)
yValues = np.arange(1, arrayLength + 1)

# random.shuffle(yValues)

fig = plt.figure(num=1)
ax = fig.add_subplot(1, 1, 1)
# bar = ax.bar(xValues,yValues)


def update(frame):
    # plt.pause(0.5)
    # plt.cla()
    shuffle(yValues)
    return ax.bar(xValues, yValues)

ani = FuncAnimation(fig, update, interval=500, blit=True)

plt.show()
