def fib(n):
    if n<=1: return 1
    else: return fib(n-1) + fib(n-2)

sum = 0
for i in range(0, 34):
    if fib(i) % 2 == 0:
        sum += fib(i)
        
print(sum)