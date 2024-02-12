
import os

# Ensure you run this script in a safe directory as it will create and delete files and directories

# Create a new directory (ensure it does not exist to avoid an error)
dir_name = 'new_directory'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f'Directory {dir_name} created')
else:
    print(f'Directory {dir_name} already exists')

# Remove the directory (ensure it exists to avoid an error)
if os.path.exists(dir_name):
    os.rmdir(dir_name)
    print(f'Directory {dir_name} removed')
else:
    print(f'Directory {dir_name} does not exist')

# Create a new file to demonstrate renaming (be cautious with file paths)
file_name = 'example_file.txt'
new_file_name = 'renamed_file.txt'
with open(file_name, 'w') as f:
    f.write('This is a test file.')

if os.path.exists(file_name):
    os.rename(file_name, new_file_name)
    print(f'File renamed from {file_name} to {new_file_name}')

# Check if the new file exists
if os.path.exists(new_file_name):
    print(f'File {new_file_name} exists')
else:
    print(f'File {new_file_name} does not exist')
