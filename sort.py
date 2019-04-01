import pprint
import random
import sys
from copy import deepcopy
from datetime import datetime
from time import sleep

from utils.output_format import print_result

a= list(range(1000))
random.shuffle(a)

def bubble_sort(array):
    '''
    Operations O(n^2), space O(1)
    :param array: List of numbers to be sorted
    :return: None
    '''
    last_idx_changed = range(len(array[:-1]))
    count = 0
    iterations = 0
    for ind in range(len(array[:-1])):
        for idx in range(len(array[:-1]) - ind):
            if array[idx] > array[idx + 1]:
                last_idx_changed = idx
                array.insert(idx, array.pop(idx + 1))
                count += 1
        iterations = ind
        if count == 0:
            break
    return array
    
def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i): 
            if arr[j] > arr[i]:
                temp = arr.pop(i)
                arr.insert(j, temp) 
    return arr

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
def get_split_point(arr, first, last):
    pivot = arr[first]
    lower = first + 1
    upper = last

    flg_done = False
    while not flg_done:
        # Increase lower until it finds a value greater than pivot
        while lower <= upper and arr[lower] <= pivot:
            lower += 1
        # Decrease upper until it finds a value lower than pivot
        while upper >= lower and arr[upper] >= pivot:
            upper -= 1

        # If there is a cross, it means upper gets lower than  lower, break the loop
        if lower > upper:
            flg_done = True
        else: # Swap upper and lower
            temp = arr[lower]
            arr[lower] = arr[upper]
            arr[upper] = temp

    # Swap positions between upper and pivot 
    temp = arr[first]
    arr[first] = arr[upper]
    arr[upper] = temp

    return upper # This is the last position of pivot

def quick_sort(arr, first, last):

    if first < last:
        split_point = get_split_point(arr, first, last)
        quick_sort(arr, first, split_point -1)
        quick_sort(arr, split_point+1, last)
        
def is_sorted(arr):
    return all([ arr[i] < arr[i+1] for i in range(len(arr)-1)])

def main(param):
    max_numbers = 20 # len(a)
    print("ORIGINAL ARRAY", str(a[:max_numbers])[:-1], " ...]" if max_numbers < len(a) else "]")
    algorithm_list = [
                      (insertion_sort, {}),
                      (merge_sort, {}),
                      (quick_sort, {'first':0,'last':len(a)-1})
            ]
    for algorithm in algorithm_list:
        print_result(org_arr=a, func=algorithm[0], args_dict=algorithm[1])

if __name__ == '__main__':
    main(sys.argv[:2])
