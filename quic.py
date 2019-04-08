log = open("log.txt" , "w")
import random

def quick_sort_ascending (arr : list) :
    global log
    print("current arr : %s" % str(arr))
    log.write("current arr : %s\n" % str(arr))
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
        log.write("p, q : %d, %d\n" % (p, q))
        print("starting pivot for this iteration : %d" % pivot)
        log.write("starting pivot for this iteration : %d\n" % pivot)
        while p != q:
            if arr[p] == arr[q] :
                random.seed(420)
                idxPvt = random.randint(0,arr.__len__())
                #pivot = arr[int(len(arr)/2)]
                pivot = arr[idxPvt]
                p = 0
                q = len(arr) - 1
                print("----- p = q")
                print("p, q : %d, %d" % (p, q))
                print("pivot for this iteration : %d" % pivot)
                print("arr[%d] , arr[%d] : %d, %d" % (p, q, arr[p], arr[q]))
                print("EOF ----- p = q")
                log.write("p, q : %d, %d\n" % (p, q))
                log.write("pivot for this iteration : %d" % pivot)
                log.write("arr[%d] , arr[%d] : %d, %d\n" % (p, q, arr[p], arr[q]))

            while arr[p] < pivot and p < q:
                p = p + 1
                print("p, q : %d, %d" % (p, q))
                print("arr[%d] , arr[%d] : %d, %d" % (p, q, arr[p], arr[q]))
                log.write("p, q : %d, %d\n" % (p, q))
                log.write("arr[%d] , arr[%d] : %d, %d\n" % (p, q, arr[p], arr[q]))
            # 1 >= 1 and 6 > 1 === true and true == true
            while arr[q] >= pivot and q > p:
                if arr[q] >= pivot and arr[q] <= pivot :
                    arr[p], arr[q] = arr[q], arr[p]
                q = q - 1
                print("p, q : %d, %d" % (p, q))
                print("arr[%d] , arr[%d] : %d, %d" % (p, q, arr[p], arr[q]))
                log.write("p, q : %d, %d\n" % (p, q))
                log.write("arr[%d] , arr[%d] : %d, %d\n" % (p, q, arr[p], arr[q]))

            # penukaran nilai
            arr[p], arr[q] = arr[q], arr[p]
            print("temp array  : %s \n" % str(arr))
            log.write("temp array  : %s \n" % str(arr))

        print("pivot for this iteration : %d" % pivot)
        print("left arr : %s " % str(arr[:arr.index(pivot)+1]))
        print("right arr : %s" % str(arr[arr.index(pivot)+1:]))
        print("Current list before split : %s" % str(arr))
        log.write("pivot for this iteration : %d\n" % pivot)
        log.write("left arr : %s\n" % str(arr[:arr.index(pivot)+1]))
        log.write("right arr : %s\n" % str(arr[arr.index(pivot)+1:]))
        log.write("Current list before split : %s\n" % str(arr))
        left = quick_sort_ascending(arr[:arr.index(pivot)+1])
        right = quick_sort_ascending(arr[arr.index(pivot)+1:])
        return ( left + right )



if __name__ == '__main__' :
#    global log
    import datetime

    #list = [12,5,6,89,31,2,3,4,5,6]
    #list = [1,3,0,1,1,7,0,3,6,3]
    list = random.sample(range(-1000000, 1000000), 100000 )
    temp = list
    #list = [0,0,3,3,1,1,2,3,4]
    #list = [0,0,1,1,3,3,4,4,5,5,6,6]
    #list = [1,3,0,1,1,7,4,4,7,3]
    #print("XXX 0- %s" % str(list[0:0]))

    # buat worst case
    list.sort(reverse=True)
    log.write(str(list) + "\n")
    start_time = datetime.datetime.now()
    x = quick_sort_ascending(list)
    end_time = datetime.datetime.now()
    #print("left : %s" % str(list[:list.index(3)]))
    #print("right : %s" % str(list[list.index(3):]))

    print("Awal sorting  : %s" % str(temp))
    print("Hasil sorting : " + str(x)+'\n')
    print("Elapsed time  : %s" % str(end_time-start_time))
    log.write("Awal sorting : %s\n" % str(temp))
    log.write("Hasil sorting : " + str(x))
    log.close()