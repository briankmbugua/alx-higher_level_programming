#!/usr/bin/python3:
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        total = 0
        count = 0
        for i in my_list:
            lst = list(i)
            val = 1
            for j in lst:
                val *= j
            total += val
            count += lst[1]
        return total/count
