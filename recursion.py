from datetime import datetime

def measure_time(f):
    def wrapper(f2, number):
        ini = datetime.now()
        res = f2(number)
        final = datetime.now()
        print('Elapse time: {}'.format(final-ini))
        
        return res
    
    return wrapper

def fibo(number):
    if number in [0, 1]:
        return 1

    return number + fibo(number - 1)

def fibo_dyn_prog(number):
    memoized = {}

    if number <= 2:
        return 1

    if number in memoized.keys():
        return memoized[number]

    res = fibo(number - 1) + fibo(number - 2)
    memoized[number] = res
    return res
 
@measure_time
def call_f(f2, num):
     return f2(num)

def main():
    number = 500
    print('Recursion fibonacci({}):{}'.format(number, call_f(fibo, number)))
    print('Recursion fibonacci({}) dynamic programming :{}'.format(number, call_f(fibo_dyn_prog, number)))

if __name__ == '__main__':
    main()
