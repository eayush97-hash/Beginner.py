# Today I learned about Operators in Python
# Operators are special symbols that perform operations on values or variables.
# There are 3 main types we covered today: Arithmetic, Comparison, and Logical operators.

# -----------------------------
# Arithmetic Operators
# These are used for basic math operations like +, -, *, / etc.

print(5 + 3)   # Addition: 5 plus 3 = 8
print(10 - 4)  # Subtraction: 10 minus 4 = 6
print(6 * 2)   # Multiplication: 6 times 2 = 12
print(7 / 2)   # Division: gives a float result → 3.5
print(7 // 2)  # Floor Division: gives only the whole number part → 3
print(7 % 2)   # Modulus: gives the remainder → 1
print(2 ** 4)  # Exponentiation: 2 to the power of 4 → 16

# -----------------------------
# Comparison Operators
# These are used to compare two values. The result is always True or False.

print(5 > 3)    # Greater than → True
print(5 < 3)    # Less than → False
print(5 >= 5)   # Greater than or equal to → True
print(5 <= 7)   # Less than or equal to → True
print(5 == 5)   # Equal to → True
print(5 != 3)   # Not equal to → True

# -----------------------------
# Logical Operators
# These combine multiple conditions.
# and → returns True if BOTH conditions are True
# or  → returns True if AT LEAST one condition is True
# not → flips the result (True becomes False, False becomes True)

print(True and True)    # Both are True → True
print(True and False)   # One is False → False
print(True or False)    # At least one is True → True
print(False or False)   # Both False → False
print(not True)         # Opposite of True → False
print(not False)        # Opposite of False → True
