
import os

# Print the current working directory
print("Current working directory:", os.getcwd())

# Change the current working directory (Modify the path as per your system)
os.chdir('/tmp')

# Print the current working directory after change
print("Directory after change:", os.getcwd())

# List directory contents
print("Directory contents:", os.listdir('.'))
