from functools import reduce
from math import sqrt

def tri(n):
    return n*(n+1)/2

def factors(n):
        step = 2 if n%2 else 1
        return len(set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0))))
    
num = 0    
for i in range(1, 100000):
    t = tri(i)
    f = factors(t)
    if f>500:
        num = t
        break

print(num)