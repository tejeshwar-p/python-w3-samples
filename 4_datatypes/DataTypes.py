# Python has the following built in data types
"""
Text type:      str
Numeric types:  int, float, complex
Sequence types: list, tuple, range
Mapping type:   dict
Set types:      set, frozenset
Boolean type:   bool
Binary types:   bytes, bytearray, memoryview
None type:      NoneType
"""

# To know the type of variable we can use the type() method
x = 5
print(type(x))

print("----------------------------------------------")
# In Python the data type is set when we assign a value to a variable;
# Examples
x = "Hello World!"
print(x)
print(type(x))
print()
x = 20
print(x)
print(type(x))
print()
x = 20.5
print(x)
print(type(x))
print()
x = 1j
print(x)
print(type(x))
print()
x = ["apple", "banana", "cherry"]
print(x)
print(type(x))
print()
x = ("mango", "orange", "grapes")
print(x)
print(type(x))
print()
x = range(6)
print(x)
print(type(x))
print()
x = {"name": "John", "age": 36}
print(x)
print(type(x))
print()
x = {"cat", "dog", "rabbit"}
print(x)
print(type(x))
print()
x = frozenset({"tiger", "lion", "cheetah"})
print(x)
print(type(x))
print()
x = True
print(x)
print(type(x))
print()
x = b"Hello"
print(x)
print(type(x))
print()
x = bytearray(5)
print(x)
print(type(x))
print()
x = memoryview(bytes(5))
print(x)
print(type(x))
print()
x = None
print(x)
print(type(x))
print("----------------------------------------------")

# If we want to specify the data type we can use the following constructor functions
x = str("Hello World!")
print(x)
print(type(x))
print()
x = int(20)
print(x)
print(type(x))
print()
x = float(20.5)
print(x)
print(type(x))
print()
x = complex(1j)
print(x)
print(type(x))
print()
x = list(("apple", "banana", "cherry"))
print(x)
print(type(x))
print()
x = tuple(("mango", "orange", "grapes"))
print(x)
print(type(x))
print()
x = range(6)
print(x)
print(type(x))
print()
x = dict(name="John", age=36)
print(x)
print(type(x))
print()
x = set(("cat", "dog", "rabbit"))
print(x)
print(type(x))
print()
x = frozenset(("tiger", "lion", "cheetah"))
print(x)
print(type(x))
print()
x = bool(5)  # True
print(x)
print(type(x))
print()
x = bytes(5)  # b"Hello"
print(x)
print(type(x))
print()
x = bytearray(5)
print(x)
print(type(x))
print()
x = memoryview(bytes(5))
print(x)
print(type(x))
print()
print("----------------------------------------------")