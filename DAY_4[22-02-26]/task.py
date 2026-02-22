# Explicit Type Casting
# x = bool(0)
# print(x, type(x))

# x = bool(56)
# print(x, type(x))

# x = bool("")
# print(x, type(x))

# x = bool("SAM")
# print(x, type(x))

# ...............................................................
# Many Values to Multiple Variables..........
# x = 45
# y = 67
# z = 90
# print(x, y, z)


# x, y, z = 45, 67, 90
# print(x, y, z)

# ...............................................................
# One Value to Multiple Variables........

# a = 12
# b = 12
# c = 12
# print(a, b, c)

# a = b = c = 12
# print(a, b, c)
# ...............................................................
# Mathematical Operators

a = 5
b = 3
# addition (+)
# print(a + b)
# subtraction (-)

# multiplication (*)

# division (/)
# print(a / b)
# modulo operator (%)
# print(a % b)
# Exponentiation Operator (**)   5**2 => 5*5  5**3 => 5*5*5
# print(a**b)
# ........................................................................
# Maths => 98
# Science => 56
# Social_Science => 90

# maths = 98
# science = 56
# social_science = 90

# Print Total Marks
# total = maths + science + social_science
# print(total)

# Print Average Marks
# average= total / number of subjects
# average = total / 3
# print(average)
# .......................................................................
# calculate the cube of a number
n = 23
# ................................................................................

"""
    ### Problem 1: Basic Calculations
    **Scenario:**
    You are helping a small retail store owner keep track of their inventory values. 
    The store has three products with the following details:
    - **Product A**: Price = 12.50, Quantity = 20
    - **Product B**: Price = 7.30, Quantity = 15
    - **Product C**: Price = 5.25, Quantity = 10
    **Tasks:**
    1. Calculate the total value of each product's inventory (Price* Quantity) and the sum of the total values of all products.
    2. Find the difference in inventory value between Product A and Product B.
    3. Compute the product of the quantities of all three products.
    4. Determine the average price of the three products (considering only the prices).
    5. Concatenate the product names and quantities into a single string and print it.
"""

priceA = 12.50
quantityA = 20
priceB, quantityB = 7.30, 15
priceC, quantityC = 5.25, 10
# print(priceA, quantityA, priceB, quantityB, priceC, quantityC)
# 1.
totalValA = priceA * quantityA
totalValB = priceB * quantityB
totalValC = priceC * quantityC
print(totalValA)
print(totalValB)
print(totalValC)
sumTotal = totalValA + totalValB + totalValC
print(sumTotal)
# ...............................................
# 2.
print(totalValA - totalValB)
