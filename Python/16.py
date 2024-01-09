import math

def getSum(n): 
    sum = 0
    for digit in str(n):  
        sum += int(digit)       
    return sum

num = int(math.pow(2, 1000))
sum = getSum(num)
print(sum)