# enumerate() example

fruits = ["Apple", "Banana", "Orange"]

print("Enumerate:")

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

print()

# zip() example

names = ["Tom", "Anna", "John"]
scores = [90, 85, 95]

print("Zip:")

for name, score in zip(names, scores):
    print(name, score)

print()

# Type checking

number = 10
text = "25"

print("Type:")
print(type(number))
print(type(text))

print()

# Type conversion

text_number = "100"
integer = int(text_number)

decimal = float(text_number)

word = str(integer)

print("Integer:", integer)
print("Float:", decimal)
print("String:", word)