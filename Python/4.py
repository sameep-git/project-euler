def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else: return False
    
ans = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        temp = x*y
        if is_palindrome(temp):
            if temp>ans: ans = temp


print(ans)