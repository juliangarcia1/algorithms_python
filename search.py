import sys
n = 20
a = list(range(n))

def binary_search(arr, value):
    '''Search a value in a ordered array
    '''
    l=len(arr)
    upper = l-1
    lower = 0
    
    while lower <= upper:
        midpoint = (upper+lower)//2
        if value == arr[midpoint]:
            return  midpoint
        elif value > arr[midpoint]:
            lower = midpoint + 1
        else:
            upper = midpoint - 1

    if lower > upper:
        return None
            
        
if  __name__ == '__main__':
    print(a)
    print(binary_search(a, 10))
