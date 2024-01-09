import math

def is_prime(n):
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True

factors = []
n = 600851475143

for x in range(2, math.floor(math.sqrt(n)) + 1):
    if is_prime(x):
        if n % x == 0:
            factors.append(x)
            n2 = n / x
            if is_prime(n2):
                factors.append(n2)

print(factors[-1])