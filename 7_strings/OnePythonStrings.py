# Strings in python can be surrounded either by single or double quotation marks
print("Hello")
print('Hello')

# assigning value to a string
a = "This is some example string"
print(a)

# multiline strings in python can be assigned using
# three double quotes
# or three single quotes
print()
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print()
b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)
print()

# Strings in python are arrays of bytes representing unicode characters
a = "Hello World!"
print(a[1])
print(a[7])
print()

# looping through a string
for x in "banana":
    print(x)
print()

# string length
print(len(a))

# check string - check if a certain phrase or character is present in a string
# we can use the keyword 'in'
txt = "The best things in life are free!"
print(txt)
print("Is 'free' present in txt? ", "free" in txt)  # is "free" present in text?
print("Is 'about' present in txt? ", "about" in txt)  # is "about" present in text?
print()

# "in var_name" can also be used in if statements
if "free" in txt:
    print("Yes, 'free' is present in txt")
print()

# check if not
txt2 = "This is some random text for testing"
print(txt2)
print("Is 'expensive' NOT present in txt? ", "expensive" not in txt2)
print("Is 'random' NOT present in txt? ", "random" not in txt2)
print()
if "expensive" not in txt2:
    print("No, 'expensive' is NOT present in txt2")
print()
