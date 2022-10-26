import random

# There are three numeric types in python
"""
int
float
complex

example -
x = 1  # int
y = 2.8  # float
z = 1j  # complex
"""

# Type conversions

x = 1
y = 2.8
z = 1j

# convert from int to float
a = float(x)
print(a)
print(type(a))
print()


# convert from float to int
b = int(y)
print(b)
print(type(b))
print()

# convert from int to complex
c = complex(x)
print(c)
print(type(c))
print()

# complex numbers cannot be converted into another type

# Random number
print(random.randrange(1, 10))


