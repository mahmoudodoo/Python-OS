
import os

# Joining paths
joined_path = os.path.join('directory', 'subdirectory', 'file.txt')
print('Joined path:', joined_path)

# Splitting paths
dir_name, file_name = os.path.split(joined_path)
print('Directory:', dir_name)
print('File Name:', file_name)

# Absolute path
absolute_path = os.path.abspath('example.txt')
print('Absolute path:', absolute_path)

# Checking if a path is absolute
print('Is absolute:', os.path.isabs(absolute_path))

# Relative path
relative_path = os.path.relpath(absolute_path, '/')
print('Relative path from root:', relative_path)
