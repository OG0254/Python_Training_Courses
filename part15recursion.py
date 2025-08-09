def iterativeFactorial(n):
    result = 1
    for i in range(n, 0, -1):
        result = result * i
    return result
    
print(iterativeFactorial(5)) # 5! > 5*4*3*2*1 = 120