import re

# Task 10

text = input("Enter camelCase text: ")


result = re.sub(
    r"([A-Z])",
    r"_\1",
    text
)


result = result.lower()


print(result)