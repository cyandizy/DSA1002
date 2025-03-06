# Source: Converted from iterative form from https://www.geeksforgeeks.org/python-program-to-find-the-gcd-of-two-numbers/#:~:text=a%20%3D%2060%20%20%20%23%20first%20number%0Ab%20%3D%2048%20%20%20%23%20second%20number%0A%0Awhile%20a%20!%3D%20b%3A%0A%20%20%20%20if%20a%20%3E%20b%3A%0A%20%20%20%20%20%20%20%20a%20%2D%3D%20b%20%20%23%20subtract%20b%20from%20a%20if%20a%20is%20greater%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20b%20%2D%3D%20a%20%20%23%20subtract%20a%20from%20b%20if%20b%20is%20greater%0A%0Aprint(a)

def gcd(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Value must be integer")

    x = abs(x)
    y = abs(y)

    if x == 0 and y != 0:
        return y
    elif y == 0 and x != 0:
        return x

    if x > y:
        return gcd(x - y, y)
    elif x < y:
        return gcd(x, y - x)
    elif x == y:
        return x

print(gcd(0, -21))