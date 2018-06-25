def fibonacci_recursive(n):
    if n is 0:
        return 0
    if n <= 2:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
def fibonacci_iterative(n):
    if n is 0:
        return 0
    i = 0
    j = 1
    k = 0
    result = 0
    while(k is not n-1):
        k = k+1
        result = i+j
        i = j
        j = result
    return result
def fibonacci_dynamic(n):
    if n is 0:
        return 0
    else:
        prev = 0
        curr = 1
        while (n > 1):
            n = n-1
            new = prev + curr
            prev = curr
            curr = new
        return curr
def fibonacci(n):
    print(fibonacci_recursive(n))
    print(fibonacci_iterative(n))
    print(fibonacci_dynamic(n))
# fibonacci(0)

def find_single_element(array):
    # Find the only element in an array that only occurs once.
    
    # 1. put items in separate arrays then check if any array have a size of 1
    # 2. use a dictionary to track how many times an item occurs in the array

    uniques = []
    keyvalue = {}
    for x in range(0, len(array)):
        print(array[x])
    pass
# find_single_element([1,2,2,3,3,5,5,5])

def multiply(i,j):
    # Write a multiply function that multiples 2 integers without using *
    if (i is 0) or (j is 0):
        return 0
    return i + multiply(i, j-1)

def multiply_main(i,j):
    print(multiply(i,j))
# multiply_main(5,2)

def find_commmon_elements(array1, array2):
    common = []
    for i in range(0, len(array1)):
        candidate = array1[i]
        if (candidate in array2) and (candidate not in common):
            common.append(candidate)
    print(common)
# find_commmon_elements([1,2,1], [3,2,1,5])

