# Write a Python script that:
# Takes a number as input.
# Prints whether it is int or float.
# Converts it into a string and shows its type.
# Stores it in a list, tuple, dict, and set, then prints each.


input = 99
print(type(input))

input = str(input)
print(type(input))

li = [1,2]
tu = (1,2)
di = {'a':1, 'b': 2}
se = {1,2}

li.append(input)
print(li)

di['c']=input
print(di)

se.add(input)
print(se)