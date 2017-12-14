# In this file, I just test the format of the output file
# There two many print here
# I may use @property to reconstruct the pointers and array
# This means I need to define new class of pivot, pointers and array


def QuickSortA(arr, low, high):
    if high <= low:
        return arr
    else:
        pivot = arr[low]
        rp = high
        lp = low + 1
        print("piviot", low, arr[low], file=stepsfile)
        print("rp", rp, arr[rp], file=stepsfile)
        print("lp", lp, arr[lp], file=stepsfile)

        print
        while lp < rp:
            while (arr[rp] > pivot) and (lp < rp):
                rp -= 1
                print("rp", rp, arr[rp], file=stepsfile)
            while (arr[lp] < pivot) and (lp < rp):
                lp += 1
                print("lp", lp, arr[lp], file=stepsfile)
            if lp == rp:
                break
            else:
                arr[lp], arr[rp] = arr[rp], arr[lp]
                print("arr", lp, rp, file=stepsfile)
        if arr[low] > arr[rp]:
            arr[low], arr[rp] = arr[rp], arr[low]
            print("arr", low, rp, file=stepsfile)
        # array index is from 0 while pivot is from 1
        QuickSortA(arr, low, pivot - 2)
        QuickSortA(arr, pivot, high)

# def DynamicPlot(frame)


if __name__ == "__main__":

    from random import shuffle
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib.animation import FuncAnimation


    len = 50
    x = np.arange(1, len + 1)
    y = np.asarray([12,32,44,50,7,17,43,37,35,41,14,21,38,8,23,26,27,18,6,34,40,1,48,24,30
,31,42,20,11,33,25,13,29,9,16,2,3,36,45,15,46,39,5,19,47,10,28,4,22,49])
    print(y)

    # shuffle(y)
    # print(y)

    stepsfile = open("steps.txt", "w")
    QuickSortA(y, 0, y.size - 1)
    stepsfile.close()

    print(y)

    fread = open("steps.txt", "r")


    fig, ax = plt.subplots()

    barPlot = plt.bar(x,y)
    fig.canvas.draw()

    for line in fread:
        stepData = line.split()
        if stepData[0] == "piviot":
            pass
        elif (stepData[0] == "rp" or stepData[0] == "lp"):
            pass
        elif stepData[0] == "arr":
            pass
        else:
            print(stepData[0])




