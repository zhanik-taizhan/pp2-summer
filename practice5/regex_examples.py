import re

# Example 1 - search()

text = "Python is easy to learn."

result = re.search(r"easy", text)

print("Search:")
print(result.group())
print()


# Example 2 - findall()

text = "Apple Orange Apple Banana Apple"

result = re.findall(r"Apple", text)

print("Findall:")
print(result)
print()


# Example 3 - split()

text = "Python,Java,C++,C#"

result = re.split(r",", text)

print("Split:")
print(result)
print()


# Example 4 - sub()

text = "I like Java."

result = re.sub(r"Java", "Python", text)

print("Sub:")
print(result)
print()


# Example 5 - Metacharacters

text = "cat bat hat"

result = re.findall(r".at", text)

print("Metacharacters (.):")
print(result)
print()


# Example 6 - Special sequences

text = "Room 15, Floor 7"

result = re.findall(r"\d+", text)

print("Special sequence (\\d):")
print(result)
print()


# Example 7 - Quantifiers

text = "ab abb abbb abbbb"

result = re.findall(r"ab{2,3}", text)

print("Quantifiers:")
print(result)