import re

# Task 5

text = input("Enter string: ")

result = re.fullmatch(
    r"a.*b",
    text
)

if result:
    print("Match found")
else:
    print("No match")