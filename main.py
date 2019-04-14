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
        #print("p, q : %d, %d" % (p, q))

  #      print("starting pivot for this iteration : %d" % pivot)

        while p != q:
            if arr[p] == arr[q] :
                random.seed(420)
                idxPvt = random.randint(0,arr.__len__())
                #pivot = arr[int(len(arr)/2)]
                pivot = arr[idxPvt]
                p = 0
                q = len(arr) - 1


            while arr[p] < pivot and p < q:
                p = p + 1

            # 1 >= 1 and 6 > 1 === true and true == true
            while arr[q] >= pivot and q > p:
                if arr[q] >= pivot and arr[q] <= pivot :
                    arr[p], arr[q] = arr[q], arr[p]
                q = q - 1


            # penukaran nilai
            arr[p], arr[q] = arr[q], arr[p]


        #print("pivot for this iteration : %d" % pivot)
        #print("left arr : %s " % str(arr[:arr.index(pivot)+1]))
        #print("right arr : %s" % str(arr[arr.index(pivot)+1:]))
        #print("Current list before split : %s" % str(arr))
        left = quick_sort_ascending(arr[:arr.index(pivot)+1])
        right = quick_sort_ascending(arr[arr.index(pivot)+1:])
        #return ( quick_sort_ascending(arr[:arr.index(pivot)+1]) + quick_sort_ascending(arr[arr.index(pivot)+1:]) )
        return (left + right)


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
    random.seed(299)
    #list = [12,5,6,89,31,2,3,4,5,6]
    #list = random.sample(range(-10000, 10000), 3929 )
    list = random.sample(range(-10000, 10000), 2000)

    #print(list)
    # buat worst case
    list.sort(reverse=True)
    print("raw list %s" % str(list))
    temp_2 = list
    start_time = datetime.datetime.now()
    x = quick_sort_ascending(list)
    end_time = datetime.datetime.now()

    start_time_2 = datetime.datetime.now()
    y = insertionSort_ascending(temp_2)
    end_time_2 = datetime.datetime.now()

    print("Quick Sort")
    print("Hasil sorting : " + str(x)+'\n')
    print("Elapsed time  : %s" % str(end_time-start_time))

    print("\nInsertion sort")
    print("Hasil sorting : " + str(y)+'\n')
    print("Elapsed time  : %s" % str(end_time_2-start_time_2))


    sys.setrecursionlimit(lim)
