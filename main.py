#import workerpool
import random

def quick_sort_ascending (arr : list) :
    # pivot is last element
    if len(arr) == 1 or len(arr) == 0 :
        return arr
    elif len(arr) == 2 :
        if arr[0] > arr[1] :
            return [arr[1],arr[0]]
        else :
            return arr
    else :
        pivot = arr[0]
        p = 0
        q = len(arr) - 1
        while p != q:
            if arr[p] == arr[q] :
                pivot = arr[random.randint(0,arr.__len__())]
                p, q = 0, len(arr) - 1
            while arr[p] < pivot and p < q:
                p = p + 1
            # 1 >= 1 and 6 > 1 === true and true == true
            while arr[q] >= pivot and q > p:
                if arr[q] >= pivot and arr[q] <= pivot :
                    arr[p], arr[q] = arr[q], arr[p]
                q = q - 1
            # penukaran nilai
            arr[p], arr[q] = arr[q], arr[p]
        return (quick_sort_ascending(arr[:arr.index(pivot)+1]) + quick_sort_ascending(arr[arr.index(pivot)+1:]))


def insertionSort_ascending(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == '__main__' :

    import datetime
    import sys
    lim = sys.getrecursionlimit()
    # set 40000 as recursion limit
    sys.setrecursionlimit(15000)
    #random.seed(299)
    #list = [12,5,6,89,31,2,3,4,5,6]
    #list = random.sample(range(-10000, 10000), 3929 )
    listo = random.sample(range(-1, 100), 15)
    #listo = [98, 91, 88, 86, 85, 78, 75, 74, 65, 57, 45, 41, 38, 23, 0]
    #print ('raw : %s' % listo)
    #print(list)
    # buat worst case
    listo.sort(reverse=True)
    print('raw : %s' % listo)
    listp = listo[:] #[98, 91, 88, 86, 85, 78, 75, 74, 65, 57, 45, 41, 38, 23, 0]
    #listx = [98, 91, 88, 86, 85, 78, 75, 74, 65, 57, 45, 41, 38, 23, 0]
    #listy = [98, 91, 88, 86, 85, 78, 75, 74, 65, 57, 45, 41, 38, 23, 0]

    start_time = datetime.datetime.now()
    x = quick_sort_ascending(listo)
    end_time = datetime.datetime.now()

    #start_time_2 = datetime.datetime.now()
    #y = insertionSort_ascending(listx)
    #end_time_2 = datetime.datetime.now()

    print("Quick Sort")
    print("List awal \t\t: ", str(listp))
    print("Hasil sorting : " + str(x)+'\n')
    print("Elapsed time  : %s" % str(end_time-start_time))

    #print("\nInsertion sort")
    #print("List awal \t\t: ", str(listy))
    #print("Hasil sorting : " + str(y)+'\n')
    #print("Elapsed time  : %s" % str(end_time_2-start_time_2))


    sys.setrecursionlimit(lim)
