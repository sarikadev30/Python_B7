# Logical Operators

# AND   => True only when all are True

# print(True and True)
# print(False and True)
# print(True and False)
# print(False and False)
# print(True and True and False)

# a = 5 > 4  # T
# b = 3 > 5  # F
# print(a and b)

# p = 3 > 5  # F
# q = 9 >= 8  # T
# print(p and q)  # F
# .................................................................

# OR => True when anyone is True

# print(True or True)
# print(False or True)
# print(True or False)
# print(False or False)
# print(True or True or False)

# p = 3 > 5  # F
# q = 9 >= 8  # T
# print(p or q)
# .................................................................
#  NOT => It will change to the opposite value

# print(not True)
# print(not False)

# z = 23 > 9
# print(not z)

# ..................................................................
# Problem :
# a = 9 < 11  # T
# b = 2 == 3  # F
# c = 10 > 3  # T
# result = a and (b or c)
# print(result)
# ...............................................
# x = 4 <= 4  # T
# y = 10 < 5  # F
# z = not (x and y)
# print(z)
# ...............................................
# m = 0 != 0  # F
# n = 1 == 1  # T
# o = m and not n
# print(o)

# .................................................................

# p = 6 == 6  # T
# q = 5 != 5  # F
# r = not (p or q)
# print(r)

# .................................................................

# p = 10 < 5  # F
# q = 3 == 3  # T
# r = 7 != 7  # F
# result = not (p or q and r)
# print(result)

# ................................................................................

# Check if the Number is Positive.
# x = 23
# print(x > 0)

# .......................................................
# Check if the Number is Negative.
# y = -90
# print(y < 0)

# .......................................................
# Check if a number is even or not
# x = 23
# print(x % 2 == 0)

# .......................................................
# Check if a number is odd or not
# x = 23
# print(x % 2 == 1)

# print(x % 2 != 0)

# .......................................................
# Check if a number is divisible by 3
# x = 90
# print(x % 3 == 0)
# ................................................................
# Assignment Operaters
x = 8

# +=   Add and assign
x += 2  # x = x + 2
print(x)  # 10

# -=   Subtract and assign
x -= 3  # x = x - 3
print(x)  # 7


# *= Multiply and assign
x *= 2  # x = x * 2
print(x)  # 14

# /= Divide and assign

x /= 2  # x = x / 2
print(x)

# ........................................................................................
