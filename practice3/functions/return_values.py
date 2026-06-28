# Function that returns a value
def multiply_numbers(first_number, second_number):
    return first_number * second_number

# Function that returns text
def create_message(student_name):
    return "Welcome, " + student_name

# Save returned values
result = multiply_numbers(8, 6)
message = create_message("Alex")

# Print results
print(result)
print(message)