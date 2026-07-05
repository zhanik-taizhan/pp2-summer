# Create a file

with open("test.txt", "w") as file:
    file.write("Hello\n")
    file.write("Python\n")
    file.write("Programming\n")

# Read all text

with open("test.txt", "r") as file:
    print("read():")
    print(file.read())

# Read first line

with open("test.txt", "r") as file:
    print("readline():")
    print(file.readline())

# Read all lines

with open("test.txt", "r") as file:
    print("readlines():")
    print(file.readlines())