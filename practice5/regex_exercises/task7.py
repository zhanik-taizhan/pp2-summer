import re

# Task 7

text = input("Enter snake_case text: ")


def convert(match):
    return match.group(1).upper()


result = re.sub(
    r"_([a-z])",
    convert,
    text
)


print(result)