import math

def is_prime(n):
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True

product = 1

for x in range(1, 21):
    if is_prime(x):
        product *= x
        
print(product)