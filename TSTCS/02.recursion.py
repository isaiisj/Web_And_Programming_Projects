# Iterative
def factorial(n):
    the_product = 1
    while n > 0:
        the_product *= n
        n = n - 1
    return the_product

# Recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
