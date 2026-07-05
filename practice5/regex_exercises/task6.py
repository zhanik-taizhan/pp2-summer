import re

# Task 6

text = input("Enter text: ")

result = re.sub(
    r"[ ,.]+",
    ":",
    text
)

print(result)