# Task 2: Using the Math Module for Calculations

# importing module
import math

# User input
n = int(input("Enter any number : "))

# Square root of the number
square_root = math.sqrt(n)
print("Square root of", n," is ",square_root)

# Natural logarithm (log base e) of the number
natural_log = math.log(n)
print("Natural logarithm of", n," is ",natural_log)

# Sine of the number (in radians)
sine = math.sin(math.radians(n))
print("Sine value of", n," is ",sine)