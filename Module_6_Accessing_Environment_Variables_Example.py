
import os

# Accessing an environment variable
path_var = os.getenv('PATH')
print('PATH variable:', path_var)

# Setting a new environment variable (This change affects only the current process and its children)
os.environ['NEW_VAR'] = 'SomeValue'
print('New variable value:', os.getenv('NEW_VAR'))

# Note: The changes made to environment variables in this script are temporary and will not affect the system environment variables.
