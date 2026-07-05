import os

# Create folders

os.makedirs("documents/text_files", exist_ok=True)
os.makedirs("documents/images", exist_ok=True)

print("Folders created.")

# Create sample files

with open("documents/text_files/file1.txt", "w") as file:
    file.write("First file")

with open("documents/text_files/file2.txt", "w") as file:
    file.write("Second file")

print("Files created.")

# List files

print("\nFiles and folders:")

for item in os.listdir("documents"):
    print(item)

# Find txt files

print("\nTXT files:")

for file in os.listdir("documents/text_files"):
    if file.endswith(".txt"):
        print(file)