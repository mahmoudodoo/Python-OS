
import subprocess

# Running a shell command
print('Running shell command: ls -l')
subprocess.run(['ls', '-l'])

# Starting a new process and getting the output
result = subprocess.run(['echo', 'Hello World'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
print('\nOutput:', result.stdout)
print('Error (if any):', result.stderr)
