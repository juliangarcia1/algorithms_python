import sys
n = 20
arr = list(range(n))

def binary_search(arr, value):
    l=len(arr)
    upper = l-1
    lower = 0
    
    while lower < upper:
        midpoint = (upper-lower)//2
        if value == arr[midpoint]:
            return  midpoint
        elif value > arr[midpoint]:
            lower = midpoint + 1
        else:
            upper = midpoint - 1

    return None
            
        
if  __name__ == '__main__':
    print(arr)
    print(binary_search(arr, 21))
