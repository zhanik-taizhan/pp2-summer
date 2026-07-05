from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map() example
squares = list(map(lambda x: x ** 2, numbers))

print("Squares:")
print(squares)

print()

# filter() example
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:")
print(even_numbers)

print()

# reduce() example
total = reduce(lambda x, y: x + y, numbers)

print("Sum:")
print(total)

print()

# Other built-in functions
print("Length:", len(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted([5, 2, 1, 4, 3]))