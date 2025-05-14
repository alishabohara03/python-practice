#Write a program using functions to find greatest of three numbers.

def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print(greatest(5, 10, 7))
