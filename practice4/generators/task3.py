# Numbers divisible by 3 and 4

def divisible_numbers(number):
    for value in range(number + 1):
        if value % 3 == 0 and value % 4 == 0:
            yield value

number = int(input("Enter number: "))

for item in divisible_numbers(number):
    print(item)