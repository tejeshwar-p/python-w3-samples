# Operators are used to perform operations on variables and values
print(10 + 5)
print()

# Arithmetic operators
print(10 + 5)  # Addition
print(10 - 4)  # Subtraction
print(10 * 5)  # Multiplication
print(10 / 5)  # Division
print(10 % 3)  # Modulus
print(10 ** 5)  # Exponentiation
print(10 // 5)  # Floor Division
print()

# Assignment Operators
x = 5  # x = 5
x += 3  # x = x + 3
x -= 3  # x = x - 3
x *= 3  # x = x * 3
x /= 3  # x = x / 3
x %= 3  # x = x % 3
x //= 3  # x = x // 3
x **= 3  # x = x ** 3
# x &= 3  # x = x & 3
# x |= 3  # x = x | 3
# x ^= 3  # x = x ^ 3
# x >>= 3  # x = x >> 3
# x <<= 3  # x = x << 3
print()

# Comparision Operators
x = 5
y = 10
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print()

# Logical Operators
# and, or, not
x = 4
print(x < 5 and x < 10)
print(x < 4 or x < 5)
print(not(x < 5 and x < 10))
print()

# Identity Operators
# They are used to compare objects, not if they are equal,
# but if they are actualy the same object with same memory location
print(x is y)
print(x is not y)
print()

# Membership Operators
# They are used to test if a sequence is presented in an object.
some_list = [99, 34, 76, 23, 16, 8, 17, 5, 20]
print(x in some_list)
print(x not in some_list)
print()

# Bitwise Operators
# & 	AND	                    Sets each bit to 1 if both bits are 1
# |	    OR	                    Sets each bit to 1 if one of two bits is 1
#  ^	XOR	                    Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	                    Inverts all the bits
# <<	Zero fill left shift    Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left,
#                               and let the rightmost bits fall off
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)
print(5 << 3)
print(5 >> 2)

