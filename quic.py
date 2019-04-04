def quick_sort_ascending (arr : list) :
    print("current arr : %s" % str(arr))
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
        print("p, q : %d, %d" % (p, q))
        print("starting pivot for this iteration : %d" % pivot)
        while p != q:
            if arr[p] == arr[q] :
                pivot = arr[int(len(arr)/2)]
                p = 0
                q = len(arr) - 1

            while arr[p] < pivot and p < q:
                p = p + 1
                print("p, q : %d, %d" % (p, q))
                print("arr[%d] , arr[%d] : %d, %d" % (p, q, arr[p], arr[q]))
            while arr[q] > pivot and q > p:
                q = q - 1
                print("p, q : %d, %d" % (p, q))
                print("arr[%d] , arr[%d] : %d, %d" % (p, q, arr[p], arr[q]))



            # penukaran nilai
            temp = arr[p]
            arr[p] = arr[q]
            arr[q] = temp

        print("pivot for this iteration : %d" % pivot)
        print("left arr : %s " % str(arr[:arr.index(pivot)+1]))
        print("right arr : %s" % str(arr[arr.index(pivot)+1:]))
        left = quick_sort_ascending(arr[:arr.index(pivot)+1])
        right = quick_sort_ascending(arr[arr.index(pivot)+1:])
        return ( left + right )


if __name__ == '__main__' :
    list = [1,2,3,4,5,6]
    #list = [3,3,0,3]
    #print("XXX 0- %s" % str(list[0:0]))
    list.sort(reverse=True)
    x = quick_sort_ascending(list)
    #print("left : %s" % str(list[:list.index(3)]))
    #print("right : %s" % str(list[list.index(3):]))

    print(x)