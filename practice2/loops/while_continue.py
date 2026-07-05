# Using continue in while loop

count = 0

while count < 6:
    count += 1

    if count == 3:
        continue   # Skip number 3

    print(count)