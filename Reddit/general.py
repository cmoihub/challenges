def fibonacci_recursive(n):
    if n is 0:
        return 0
    elif n is 1 or n is 2:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
def fibonacci_iterative(n):

    return n

def fibonacci(n):
    result0 = fibonacci_recursive(n)
    result1 = fibonacci_iterative(n)
    print(result0)
    print(result1)
fibonacci(7)

def multiply(i,j):
    if (i is 0) or (j is 0):
        return 0