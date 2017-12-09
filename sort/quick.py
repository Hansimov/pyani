"""
() = QuickSort()


Inputs:
    arrayIn    :
    pivotValue :
    pivotIndex :
    lp         : Left Pointer
    rp         : Right Pointer


Outputs:
    arrayOut
    isSorted    : True, False
    pivotValue
    pivotIndex
    lp:         Left Pointer
    rp:         Right Pointer

"""

"""
Questions:
Choose what mark point as return ?

"""


def QuickSort(arr):
    if arr.size == 1 or arr.size == 0:
        return arr
    else:
        pivot = arr[0]
        lp = 1
        rp = arr.size - 1
        while lp < rp:
            while arr[rp] > pivot:
                if lp == rp:
                    break
                rp -= 1
            if lp == rp:
                break
            while arr[lp] < pivot:
                lp += 1
            arr[lp], arr[rp] = arr[rp], arr[lp]
            print(arr)
        arr[0], arr[rp] = arr[rp], arr[0]


def QSort(arr, low, high):
    print("low:"+str(low)+" - "+"high:"+str(high))
    if high <= low :
        return arr
    else:
        pivot = arr[low]
        lp = low + 1
        rp = high
        while lp < rp:
            while (arr[rp] > pivot) and (lp < rp):
                rp -= 1
            while (arr[lp] < pivot) and (lp < rp):
                lp += 1
                # print("lp:" + str(lp))
                # print("rp:" + str(rp))
            arr[lp], arr[rp] = arr[rp], arr[lp]
            print(arr)
        if arr[low] > arr[rp]:
            arr[low], arr[rp] = arr[rp], arr[low]
            print(arr)

        QSort(arr, low, pivot - 2) # array index is from 0 while pivot is from 1
        QSort(arr, pivot, high)

# if __name__ == "__main__":

from random import shuffle
import numpy as np

len = 100
a = np.arange(1, len+1)
print(a)

shuffle(a)
# a = np.asarray([9,5,6,4,8,3,2,10,1,7])
print(a)

# QuickSort(a,0,a.size-1)
QSort(a, 0, a.size - 1)
print(a)
