# Generator for squares

def squares(number):
    for value in range(number + 1):
        yield value ** 2

for item in squares(5):
    print(item)