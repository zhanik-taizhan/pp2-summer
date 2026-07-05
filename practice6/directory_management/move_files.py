import os
import shutil

# Create folders

os.makedirs("source", exist_ok=True)
os.makedirs("destination", exist_ok=True)

# Create file

with open("source/example.txt", "w") as file:
    file.write("Python Practice")

print("File created.")

# Copy file

shutil.copy("source/example.txt", "destination/example_copy.txt")
print("File copied.")

# Move file

shutil.move("source/example.txt", "destination/example.txt")
print("File moved.")