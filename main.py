import sys
import random
import pprint
from time import sleep
from copy import deepcopy


a= list(range(100))
random.shuffle(a)


def buble_sort(array):
    '''
    Operations O(n^2), space O(1)
    :param array: List of numbers to be sorted
    :return: None
    '''
    flg_changed = False
    last_idx_changed=range(len(array[:-1]))
    count = 0
    iterations = 0
    for ind in range(len(array[:-1])):
        for idx in range(len(array[:-1]) - ind):
            if array[idx] > array[idx + 1]:
                last_idx_changed=idx
                array.insert(idx, array.pop(idx + 1))
                count += 1
        iterations = ind
        if count == 0:
            break
    return array
def order_two_arrays(res, l_arr, r_arr):
    i, j, k= (0, 0, 0)
    while i < len(l_arr) and j < len(r_arr):
        if l_arr[i] >= r_arr[j]:
            res[k] = r_arr[j]   
            j += 1
        else:
            res[k] = l_arr[i]
            i += 1
        k += 1
    while i < len(l_arr):
        res[k] = l_arr[i]
        i += 1
        k += 1

    while j < len(r_arr):
        res[k] = r_arr[j]
        j += 1
        k += 1

    return res

def merge_sort(arr):
    l = len(arr)
    l_arr = arr[:int(l/2)]
    r_arr = arr[int(l/2):]

    if l > 1:
        l_res = merge_sort(l_arr)
        r_res = merge_sort(r_arr)
        res =  order_two_arrays(arr, l_res, r_res)
        return res
    else:
        return arr
        



def main(param):
    max_numbers = 20
    pprint.pprint(a,width=80, compact=True)
    print("ORIGINAL ARRAY", str(a[:max_numbers])[:-1], " ...]" if max_numbers < len(a) else "]")
    from datetime import datetime

    print("*"*15, "Bubble Sort", "*"*15)
    b = deepcopy(a)
    time_start = datetime.now()
    res_bs = buble_sort(b)
    time_end = datetime.now()
    print("Buble sort:", str(res_bs[:max_numbers])[:-1], " ...]" if max_numbers < len(a) else "]" )
    print("Consumed time:", time_end - time_start)

    print("*"*15, "Merge Sort", "*"*15)
    c = deepcopy(a)
    print('Input c:', str(c[:max_numbers])[:-1], " ...]" if max_numbers < len(a) else "]")
    time_start = datetime.now()
    res_ms = merge_sort(c)
    time_end = datetime.now()
    print("Merge sort:", str(res_ms[:max_numbers])[:-1], " ...]" if max_numbers < len(a) else "]" )
    print("Consumed time:", time_end - time_start)


if __name__ == '__main__':
    main(sys.argv[:2])
