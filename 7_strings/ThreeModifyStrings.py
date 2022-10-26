# Python has set of built-in methods that you can use to modify strings


a = "Hello World!"
print("Normal:", a)
# upper case
print("Upper:", a.upper())
# lower case
print("Lower:", a.lower())

# remove whitespace
b = " Hello, World! "
print("After removing leading and trailing white spaces:", a.strip())

# replace string
c = "This is mode"
print("Original:", c)
print("Modified:", c.replace("m", "c"))

# split string
d = "Hello, World!"
print(d.split(","))  # returns a list of strings
