def collatz(n):
    if n==1: return 0
    if n%2==0: return 1 + collatz(n/2)
    else: return 1 + collatz(3*n+1)
    
max = 0
ans = 0
for i in range(1, 1000001):
    curr = collatz(i)
    if curr > max:
        max = curr
        ans = i
        
print(ans, max)