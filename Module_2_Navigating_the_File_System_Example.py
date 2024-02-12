
import os

# Get the current working directory
print('Current Directory:', os.getcwd())

# Change the current working directory
# Ensure '/tmp' exists or choose an appropriate directory according to your operating system
os.chdir('/tmp')
print('Directory after change:', os.getcwd())

# List contents of the current directory
print('Contents:', os.listdir('.'))
