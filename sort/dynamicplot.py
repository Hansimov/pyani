# def animate(frameno):

def animate():
    for line in fread:
        # sleep(0.03)
        stepData = line.split()
        if stepData[0] == "piviot":
            piviotIndex = int(stepData[1])
            bar[piviotIndex].set_color('g')
        elif (stepData[0] == "rp" or stepData[0] == "lp"):
            pointerIndex = int(stepData[1])
            bar[pointerIndex].set_color('r')
        elif stepData[0] == "arr":
            lp = int(stepData[1])
            rp = int(stepData[2])
            lph = bar[lp].get_height()
            rph = bar[rp].get_height()
            bar[lp].set_height(rph)
            bar[rp].set_height(lph)
        else:
            print(stepData[0])

if __name__ == "__main__":

    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib.animation import FuncAnimation
    from random import shuffle
    from time import sleep as sleep


    len = 50
    x = np.arange(1, len + 1)
    # y = np.arange(1, len + 1)
    # shuffle(y)
    y = np.asarray([12,32,44,50,7,17,43,37,35,41,14,21,38,8,23,26,27,18,6,34,40,1,48,24,30
,31,42,20,11,33,25,13,29,9,16,2,3,36,45,15,46,39,5,19,47,10,28,4,22,49])


    # plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    bar = plt.bar(x,y)

    fig.canvas.draw()
    # sleep(0.3)

    fread = open("steps.txt", "r")

    piviotIndex = 0
    lp = 0
    rp = 0
    animate()

    # fig.canvas.draw_idle()
    # fig.canvas.start_event_loop(interval)

    plt.show(block=True)