def iterative_factorial(n):
    if n < 0:
        raise ValueError("Factorial must be non-negative.")
    
    result = 1
    for i in range(n, 0, -1):
        result *= i
    
    return result

def recursive_factorial(n):
    if n < 0:
        raise ValueError("Factorial must be non-negative.")
    
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)

def iterative_fibonacci(nth):
    if nth < 0:
        raise ValueError("Nth fibonacci must be non-negative.")

    previous = 0
    current = 1
    result = 0

    if nth == 1:
        result = 0
    elif nth == 2:
        result = 1
    else:
        for i in range(2, nth):
            result = previous + current
            previous = current
            current = result
    
    return result
            

def recursive_fibonacci(nth):
    if nth < 0:
        raise ValueError("Nth fibonacci must be non-negative.")
    
    if nth == 1:
        return 0
    elif nth == 2:
        return 1
    else:
        return recursive_fibonacci(nth - 1) + recursive_fibonacci(nth - 2)


try:
    print(iterative_factorial(100))

    print(recursive_factorial(997)) # cannot go any higher

    print(iterative_fibonacci(5))

    print(recursive_fibonacci(3)) # cannot go any higher and is very slow

except TypeError as e:
    print(f"Invalid input type: {e}")
