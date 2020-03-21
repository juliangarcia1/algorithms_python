"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
import copy
def permutate(array_org, n_two):
    array = copy.deepcopy(array_org)
    i = 0
    res=[]
    while i+n_two < len(array):
        temp = array[i]
        array[i] = array[n_two+i]
        array[n_two+i] = temp
        i+=1
        res.append(copy.deepcopy(array))
    return res

def climbStairs(n):
    res = []
    x=0
    while x*2<=n:
        n_one = n-(x*2)
        n_two = x
        item = [2]*(n_two)
        item += [1]*(n_one)
        res.append(item)
        if x>0 and x*2<n: res+=permutate(item,n_two)
        x+=1
    return res

import pprint
# pprint.pprint(climbStairs(1))
# pprint.pprint(climbStairs(2))
# pprint.pprint(climbStairs(3))
# pprint.pprint(climbStairs(4))
pprint.pprint(climbStairs(7))
# pprint.pprint(climbStairs(6))
# pprint.pprint(climbStairs(8))
""" Explanation          
2=1+1, 2    
3=1+1+1, 2+1
4=1+1+1+1, 2+1+1, 2+2 
5=1+1+1+1+1, 2+1+1+1, 2+2+1
6=1+1+1+1+1+1, 2+1+1+1+1, 2+2+1+1, 2+2+2

If even, example 6
1*n, 2+1*(n-2),  2+2+1*(n-4), 2+2+2
1*n, 2*1+1*(n-2), 2*2+1*(n-4), 2*3+1*(n-6)
Formula:
2*(0)+1*n, 2*(1)+1*(n-2), 2*(2)+1*(n-4), 2*(3)+1*(n-6)  # until n<=N

if odd, example 5
1*n, 2+1*(n-2),  2+2+1*(n-4)
1*n, 2*1+1*(n-2), 2*2+1*(n-4)
Formula:
2*(0)+1*n, 2*(1)+1*(n-2), 2*(2)+1*(n-4)   # Until n<=N
"""