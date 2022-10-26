# Booleans represent one of two values: True or False
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Booleans in if else conditions
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print()
# Evaluate Values and Variables
# The bool() function allows us to evaluate any value, and give us True or False in return
print(bool("Hello"))
print(bool(15))
print()

# Evaluate two variables
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
print()

# Most values are True
# If any values has content then it is mostly evaluated to true
# Any string is True except empty strings
# Any number is True except 0
# Any list, tuple, set and dictionary are True, except empty ones
print(bool("abc"))
print(bool(123))
print(bool(["apple", "banana", "cherry"]))
print()

# Some values are False
# All empty values, 0, None and False evaluate to False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print()


# Object which is having __len__(self) function which returns 0
# For example -
class MyClass:
    def __len__(self):
        return 0


my_obj = MyClass()
print(bool(my_obj))


# Functions can return a boolean
def my_function():
    return True


print(my_function())


# Code can be executed based on the Boolean answer of a function
def my_function_2():
    return True


if my_function_2():
    print("YES!")
else:
    print("NO")


# Python also has built-in functions that return a boolean value like
# isinstance() function which can be used to determine if an object is of a certain data type
x = 200
print(isinstance(x, int))

