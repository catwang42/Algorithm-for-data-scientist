#Fibonacci
from typing import List, Dict, Tuple, Set
def fib(x:int)->int:
    if x < 0:
        raise("negative value ")
    elif x<=1:
        return x
    else:
        return(fib(x-1)+fib(x-2))
    
[fib(x) for x in range(10)]

#dynamic programming 
def fib_dp(x:int)->int:
    mome = [None]*(x+1) #1 larger than number 
    if mome[x] is not None:
        return mome[x]
    if x <0:
        raise("Negative value is not accpetible")
    elif x==1 or x ==2:
        result = 1 
    else:
        result = fib_dp(x-1)+fib_dp(x-2)
    mome[x] = result 
    return result 

def fib_bottom_up(x:int)->int:
    if x==1 or x==2:
        result = 1 
    else:
        mome = [0]+[None]*(x)

        mome[1], mome[2] = 1 , 1  
        for i in range(3, n+1):
            mome[x] = mome(x-1)+mome(x-2)
        result = mome[x]
    return result  

def fib1():
    a, b = 0,1
    while True:
        yield a 
        a , b = b, a+b 
