# Contant time O(1)
customers = ["Lexi", "Britney", "Danny", "bobbi", "chris"]
free_books = customers[0]

# Linear time O(n)
free_book = False
customers = ["Lexi", "Britney", "Danny", "bobbi", "chris"]
for customer in customers:
    if customer[0] == 'B':
        print(customer)

# Quadratic time O(n^2)
numbers = [1,2,3,4,5]
for i in numbers:
    for j in numbers:
        x = i * j
        print(x)

# Cubic time 
numbers = [1,2,3,4,5]
for i in numbers:
    for j in numbers:
        for h in numbers:
            x = i + j + h
            print(x)

# Exponential time
pin = 931
n = len(str(pin))
for i in range(10**n):
    if i == pin:
        print(i)