import re

# Task 2

text = input("Enter string: ")

result = re.fullmatch(r"ab{2,3}", text)

if result:
    print("Match found")
else:
    print("No match")