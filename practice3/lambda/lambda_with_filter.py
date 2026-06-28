# Using lambda with filter()

numbers = [5, 10, 15, 20, 25, 30]

# Keep numbers greater than 15
filtered_numbers = list(filter(lambda number: number > 15, numbers))

print(filtered_numbers)