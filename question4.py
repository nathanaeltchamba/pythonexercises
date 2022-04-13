def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

x = 8
for i in range(x+1):
    print(f"Iteration {i-1}: {fib(i)}")
    
def diffNums(num):
    if num > 1:
        print(f"diffNums({num}) = diffNums({num-1}) + diffNums({num-2})")
        return diffNums(num-1) + diffNums(num-2)
    else:
        return 1
diffNums(5)