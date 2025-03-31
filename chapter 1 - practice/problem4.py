import os

# Specify the directory path
directory_path = '/python'

# List all entries in the directory
entries = os.listdir(directory_path)

# Iterate over the entries and print them
for entry in entries:
    print(entry)
    # printing
print(entries)
