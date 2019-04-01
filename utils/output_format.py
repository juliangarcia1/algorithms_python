from copy import deepcopy
from datetime import datetime

def print_result(org_arr, func, args_dict=None, max_numbers=20, print_res=True):
    '''Print the returned value from a function
       Args:
        org_arr (list): List of elements.
        func (function): Function to process list of elements.
        args_dict (dict): Extra params to pass to func.
        max_numbers (int): Maximum number of elements of list to be displayed.
        print_res (boolean): Enable/disable the print of the result.


    Returns:
        bool: The return value. True for success, False otherwise.
    '''
    title = func.__name__.replace('_', ' ').title()
    print("*"*15, title, "*"*15)

    c = deepcopy(org_arr)
    if print_res:
        print('Input: ', str(c[:max_numbers])[:-1], " ...]" if max_numbers < len(org_arr) else "]")
    time_start = datetime.now()
    res_alg = func(c, **args_dict) if args_dict else func(c)
    res_alg = c if args_dict else res_alg
    time_end = datetime.now()
    print('Lenght of array:', len(org_arr))
    if print_res:
        print(title, ": ",
              str(res_alg[:max_numbers])[:-1], " ...]" if max_numbers < len(org_arr) else "]")
    print("Elapsed time:", time_end - time_start)
