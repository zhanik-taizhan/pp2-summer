# Create and write a file

with open("test.txt", "w") as file:
    file.write("Hello\n")
    file.write("Python\n")
    file.write("Programming\n")

print("File created.")

# Add new text

with open("test.txt", "a") as file:
    file.write("New line.\n")

print("Text added.")