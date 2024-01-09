import math

def is_prime(n):
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True

cnt = 0
prime = 0

for x in range(2, 1000000):
    if is_prime(x):
        cnt+=1
    if cnt==10001:
        prime = x
        break

print(prime)
print(cnt)