
def recursive_factorial(num):
    if num == 0:
        return 1  # Base case: 0! is defined as 1
    else:
        return num * recursive_factorial(num - 1)  # General case: n! = n * (n - 1)!

print('recursive')
print(recursive_factorial(9))
print(recursive_factorial(10))
print(recursive_factorial(99))

def iterative_factorial(num):
    ans = 1
    for i in range(num, 1, -1):  # Loop from num down to 2
        ans *= i  # Multiply ans by i in each iteration
    return ans

print('iterative')
print(iterative_factorial(9))
print(iterative_factorial(20))
print(iterative_factorial(99))