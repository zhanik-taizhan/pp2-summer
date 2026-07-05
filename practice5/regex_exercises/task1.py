import re

# Task 1

text = input("Enter string: ")

result = re.fullmatch(r"ab*", text)

if result:
    print("Match found")
else:
    print("No match")