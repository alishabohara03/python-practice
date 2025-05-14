#Write a recursive function to calculate the sum of first n natural numbers.


def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)

print(recursive_sum(5))  # Output: 15