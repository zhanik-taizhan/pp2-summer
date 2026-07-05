import shutil
import os

# Create a file

with open("test.txt", "w") as file:
    file.write("Python File Handling")

# Copy file

shutil.copy("test.txt", "backup.txt")
print("File copied.")

# Delete backup

if os.path.exists("backup.txt"):
    os.remove("backup.txt")
    print("Backup deleted.")