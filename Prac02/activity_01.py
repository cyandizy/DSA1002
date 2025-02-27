import sys

def iterative_factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    
    return result

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)

def iterative_fibonacci(nth):
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
    if nth == 1:
        return 0
    elif nth == 2:
        return 1
    else:
        return recursive_fibonacci(nth - 1) + recursive_fibonacci(nth - 2)

if len(sys.argv) < 4:
    sys.exit()

if sys.argv[2] == "fa":
    if sys.argv[3] == "i":
        print(iterative_factorial(int(sys.argv[1])))
    elif sys.argv[3] == "r":
        print(recursive_factorial(int(sys.argv[1])))

elif sys.argv[2] == "fi":
    if sys.argv[3] == "i":
        print([iterative_fibonacci(i) for i in range(1, int(sys.argv[1]))])
    elif sys.argv[3] == "r":
        print([recursive_fibonacci(i) for i in range(1, int(sys.argv[1]))])
