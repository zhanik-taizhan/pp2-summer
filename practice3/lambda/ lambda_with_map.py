# Using lambda with map()

numbers = [2, 4, 6, 8]

# Multiply every number by 3
result = list(map(lambda number: number * 3, numbers))

print(result)