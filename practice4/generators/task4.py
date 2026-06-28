# Squares from a to b

def squares(start, end):
    for value in range(start, end + 1):
        yield value ** 2

for item in squares(3, 8):
    print(item)