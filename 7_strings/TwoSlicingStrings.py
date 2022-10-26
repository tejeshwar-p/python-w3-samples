# We can return a range of characters by using the slice syntax
b = "Hello World!"
print(b[2:7])   # Here start is inclusive and end is exclusive
print(b[:5])    # Here if start is not given then slicing will start from 1st character - 0th index
print(b[2:])    # Here if end is not given then slicing will end till last character - nth index

# Negative indexing -
# Use negative indexes to start the slice from the end of the string
print(b[-5:-2])
print(b[:-2])
print(b[-3:])


