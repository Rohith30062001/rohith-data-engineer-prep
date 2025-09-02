# Take a string = "PythonProgramming".
# Print first 6 characters.
# Print last 5 characters.
# Reverse the string.

string = "PythonProgramming"
print(string[:6])
print(string[-5:])
print(string[::-1])

string = f"My name is Alice and I am {25} years old."
print(string)

string = "My name is Alice and I am {age} years old."
print(string.format(age=25))

import re

text = "Error: Disk full at 12:30, Warning: CPU high at 13:10, Error: Memory leak at 14:05"

# Regex to match "Error: <message> at <time>"
pattern = r"Error: (.*?) at (\d{2}:\d{2})"

matches = re.findall(pattern, text)

print(matches)
