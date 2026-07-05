import re

# Task 8

text = input("Enter camelCase text: ")


result = re.split(
    r"(?=[A-Z])",
    text
)


print(result)