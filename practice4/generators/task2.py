# Print even numbers

def even_numbers(number):
    for value in range(number + 1):
        if value % 2 == 0:
            yield value

number = int(input("Enter number: "))

print(*even_numbers(number), sep=", ")