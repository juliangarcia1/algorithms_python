################################################################################
#########################  Binary Tree  ########################################
################################################################################
import pprint
import sys
from source.rand_nums import rand_10


def swap_values(array, idx_src, idx_dst):
    """
        Swap array values
    """
    temp = array[idx_src]
    array[idx_src] = array[idx_dst]
    array[idx_dst] = temp


def get_min(a, b):
    """
        a tuple: containing a_value and a_index inside an array
        b tuple: containing b_value and b_index inside an array
        return: idx of greatest value
    """
    a_val, a_idx = a
    b_val, b_idx = b
    return a_idx if a_val >= b_val else b_idx


def get_parent(idx):
    if idx == 0: return None
    return (idx - 1) // 2


def get_right_child(p):
    return 2 * p + 2


def get_left_child(p):
    return 2 * p + 1
    # return result if result <= lenght - 1 else None


def heapify(array, node):
    l = len(array)-1
    l_node = get_left_child(node)
    r_node = get_right_child(node)

    if l_node <= l and array[node] > array[l_node]:
        smallest = l_node 
    else: 
        smallest = node

    if r_node <= l and array[smallest] > array[r_node]:
        smallest = r_node

    if smallest != node:
        swap_values(array, smallest, node)
        heapify(array, smallest)




def min_heap(array, node_idx):
    heapify(array, node_idx)


if __name__ == '__main__':
    import math
    array = rand_10
    print(array)
    l=len(array)
    for i in range(math.ceil(l/2))[::-1]:
        min_heap(array, i)
        print(array)
