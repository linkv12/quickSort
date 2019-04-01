def quicksortAsc (list : list) :
    print("current list : %s" % (str(list)))
    if len(list) == 1 or len(list) == 0:
        return list
    elif len(list) == 2 :
        if (list[1] < list[0]) :
            return ([list[1], list[0]])
        else :
            return list
    else :
        import random
        print("seed = %s" % int(list[0]))
        random.seed(list[0])
        length = len(list)
        idxPivot = random.randint(0,length-1)
        #print(idxPivot)
        pivot = list[idxPivot]
        idxP, idxQ = 0, length - 1
        while (idxP != idxQ) :
        #    print("current list : ", end='')
        #    print(list)
            if (list[idxP] == list[idxQ]) :
                # get new pivot
                print("seed = %s" % int(list[0]))
                random.seed(length)
                idxPivot = random.randint(0, length - 1)
                pivot = list[idxPivot]
                # reset p and q
                idxP, idxQ = 0, length - 1
            else :
                if (list[idxP] > pivot) :
                    if (list[idxQ] <= pivot) :
                        temp = list[idxP]
                        list[idxP] = list[idxQ]
                        list[idxQ] = temp
                        idxQ = idxQ - 1
                        idxP = idxP + 1
                    elif (list[idxQ] > pivot) :
                        idxQ = idxQ - 1
                        if ((idxP == idxQ)) :
                            break
                elif (list[idxP] < pivot) :
                        idxP = idxP + 1
                        if (idxP == idxQ) :
                            break


        left_list = quicksortAsc(list[0:idxPivot])
        right_list = quicksortAsc(list[idxPivot:length])
        print("left list  : %s" % str(left_list))
        print("left list  : %s" % str(left_list))
        return (left_list + right_list)






if __name__ == '__main__' :
    list = [1,2,3,4,5]
    list.sort(reverse=True)
    x = quicksortAsc(list)
    print(x)