
def QuickSort(arr, low, high):
    if high <= low:
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
            arr[lp], arr[rp] = arr[rp], arr[lp]
        if arr[low] > arr[rp]:
            arr[low], arr[rp] = arr[rp], arr[low]

        # array index is from 0 while pivot is from 1
        QuickSort(arr, low, pivot - 2)
        QuickSort(arr, pivot, high)

def QuickSortA(arr, low, high):
    if high <= low:
        return arr
    else:
        pivot = arr[low]; print("pivot -",pivot)
        lp = low + 1; print("lp -",lp, arr[lp])
        rp = high; print("rp -",rp,arr[rp])
        while lp < rp:
            while (arr[rp] > pivot) and (lp < rp):
                rp -= 1; print("rp >",rp,arr[rp])
            while (arr[lp] < pivot) and (lp < rp):
                lp += 1; print("lp >", lp,arr[lp])
            if lp == rp: break
            arr[lp], arr[rp] = arr[rp], arr[lp]
            print("arr >" ,arr[lp], "<>" ,arr[rp])
        if arr[low] > arr[rp]:
            arr[low], arr[rp] = arr[rp], arr[low]
            print("arr >" ,arr[low], "<>" ,arr[rp],"...")

        # array index is from 0 while pivot is from 1
        QuickSortA(arr, low, pivot - 2)
        QuickSortA(arr, pivot, high)


if __name__ == "__main__":

    from random import shuffle
    import numpy as np

    len = 50
    a = np.arange(1, len + 1)
    print(a)

    shuffle(a)
    # a = np.asarray([9,5,6,4,8,3,2,10,1,7])
    print(a)

    QuickSortA(a, 0, a.size - 1)
    print(a)
