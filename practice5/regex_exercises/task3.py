import re

# Task 3

text = input("Enter text: ")

result = re.findall(
    r"[a-z]+_[a-z]+",
    text
)

print("Found:", result)