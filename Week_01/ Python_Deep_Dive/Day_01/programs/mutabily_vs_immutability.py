# Demonstrate:
# Modify an element of a list (mutable).
# Try to modify a tuple element (immutable → should error).
# Modify a dict value and a set by adding/removing elements.

li = [1,2,3]
tu = (1,2,3)
di = {'a': 1, 'b': 2}
se = {1,2,3}

li[0]=0
print(li)

try:
    tu[0]=0
except Exception as e:
    print(e)

di['d'] = 0
print(di)

se.pop()
print(se)