# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

x = "Hello World"
print(f'Data: {x}, Type: {type(x)}')

x = 20
print(f'Data: {x}, Type: {type(x)}')

x = 20.5
print(f'Data: {x}, Type: {type(x)}')

x = 1j
print(f'Data: {x}, Type: {type(x)}')

x = ["apple", "banana", "cherry"]
print(f'Data: {x}, Type: {type(x)}')

x = ("apple", "banana", "cherry")
print(f'Data: {x}, Type: {type(x)}')

x = range(6)
print(f'Data: {x}, Type: {type(x)}')

x = {"name" : "John", "age" : 36}
print(f'Data: {x}, Type: {type(x)}')

x = {"apple", "banana", "cherry"}
print(f'Data: {x}, Type: {type(x)}')

x = frozenset({"apple", "banana", "cherry"})
print(f'Data: {x}, Type: {type(x)}')

x = True
print(f'Data: {x}, Type: {type(x)}')

x = b"Hello"
print(f'Data: {x}, Type: {type(x)}')

x = bytearray(5)
print(f'Data: {x}, Type: {type(x)}')

x = memoryview(bytes(5))
print(f'Data: {x}, Type: {type(x)}')

x = None
print(f'Data: {x}, Type: {type(x)}')




x = 1
y = 3565622255488771112222278967236573653756375637567365723657326592356327567365823
z = -3255522622255488771112222278967236573653756375637567365723657326592356327567365823
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.


print(type(x))
print(type(y))
print(type(z))


x = 1.10
y = 1.0
z = -35.59
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100

print(x, type(x))
print(y,type(y))
print(type(z))



# Types of Casting
# Explicit Casting (Type Conversion) → done manually using functions.
# Implicit Casting (Type Promotion) → done automatically by Python when safe.

## Implicit casting
x = 5      # int
y = 2.0    # float
z = x + y  # result auto becomes float

print(z)        # 7.0
print(type(z))  # <class 'float'>

## Explicit casting
a="123"
b= int(a)
print(b, type(b))

# Slicing Strings
a = '   Rohith  '
# Slice from start to 2 values
print(a[:2])
# Slice from start to 2 values
print(a[0:2])

print(a[-5:-2])

print(a[::-1])

print(a[::-2])


print(a.upper())
print(a.lower())

print(a.replace('Ro', 'Mo'))

print(a.lstrip())
print(a.rstrip())
print(a.strip())


a="Rohith is noob"

print(a.split(' ', -1))
# It takes seperator and max number of splits, By default -1 equals to infinity

a = "Hello"
b = "World"
c = a + b
print(c)

c = a + ' ' + b
print(c)

txt = "We are the so-called \"Vikings\" from the north."

print(txt)


# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

a=[1,2,3,1]
b=(1,2,3,1)
c={1,2,3,1}
d={'a':1, 'b':2}

print(a)
print(b)
print(c)
print(c)
print(d)


li = ['apple', 'banana', 'mango']
print(li)

for i in li:
    print(i)

for i in range(len(li)):
    print(li[i])
    
i=0
while i<len(li):
    print(li[i])
    i+=1
    
# newlist = [expression for item in iterable if condition == True]
new_li = [i for i in li if 'an' in i]
print(new_li)


# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
list1 = [1,2,3]
list2 = list1 
list3=list1.copy()

list1.append(4)
print(list2)
print(list3)

