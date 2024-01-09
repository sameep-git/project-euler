import math

def isPerfectSquare(n):
    sqr = math.sqrt(n)
    return sqr.is_integer()
    
N = 1001
ans = 0
A = 0
B = 0
C = 0
for a in range(0, N):
    for b in range(a+1, N):
        if (a+b) > 1000: continue
        elif (a+b) < 1000:
            square = a*a + b*b
            if isPerfectSquare(square) and (a+b+math.sqrt(square)==1000):
                ans = a*b*(math.sqrt(square))
                A = a
                B = b
                C = math.sqrt(square)


print(ans)
print(A, B, C)