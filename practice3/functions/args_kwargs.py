# Function using *args
def total_score(*scores):
    print("Scores:", scores)
    print("Total:", sum(scores))

# Function using **kwargs
def student_information(**information):
    for key, value in information.items():
        print(key + ":", value)

# Call the functions
total_score(10, 20, 30, 40)

student_information(
    name="Alex",
    age=19,
    city="Almaty"
)