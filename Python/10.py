import math

def is_prime(n):
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True

ans = 0
for x in range(2, 2000000):
    if is_prime(x):
        ans += x
        
print(ans)