# Use comprehensions:

# Generate a list of squares of numbers 1–10.
# Generate a list of even numbers from 1–20.
# Generate a dict of numbers 1–5 with values = their cubes ({1:1, 2:8, ...}).
# Extract all vowels from a given string in a list comprehension.

list_of_squares = [x*x for x in range(1,11)]
print(list_of_squares)
list_even_nums = [x for x in range(1,21) if x%2==0]
print(list_even_nums)
dict_of_nums = {x: x*x*x for x in range(1,6)}
print(dict_of_nums)

string = 'apple'
vowels = [x for x in string if x.lower() in ['a', 'e', 'i', 'o', 'u']]
print(vowels)