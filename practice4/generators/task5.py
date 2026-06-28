# Countdown generator

def countdown(number):
    while number >= 0:
        yield number
        number -= 1

number = int(input("Enter number: "))

for item in countdown(number):
    print(item)