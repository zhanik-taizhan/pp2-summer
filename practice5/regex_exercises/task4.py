import re

# Task 4

text = input("Enter text: ")

result = re.findall(
    r"[A-Z][a-z]+",
    text
)

print("Found:", result)