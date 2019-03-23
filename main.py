import sys
import random
from time import sleep


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
    print('Initial a:          {}'.format(array))
    count = 0
    iterations = 0
    for ind in range(len(array[:-1])):
        for idx in range(len(array[:-1]) - ind):
            if array[idx] < array[idx + 1]:
                last_idx_changed=idx
                array.insert(idx, array.pop(idx + 1))
                count += 1
        iterations = ind
        if count == 0:
            break
    print('After Bubble Sort a:{} \n {} times'.format(array, iterations))


def main(param):
    buble_sort(a)


if __name__ == '__main__':
    main(sys.argv[:2])
