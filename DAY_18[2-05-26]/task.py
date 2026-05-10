# TUPLE

# CRUD => CREATE READ UPDATE DELETE

# CREATE
# 1. Way
# x = (2, 3, 4, 5, 6, 1, 23, 34, 56)
# print(x, type(x))

# 2nd way

# y = tuple((2, 3, 4, 12, 123, 123, 456, 789, 125, 567))
# print(y, type(y))

# Convert list to tuple
# a = [23, 45, 67, 89, 12, 34, 78]
# x = tuple(a)
# print(x, type(x))

# convert set to tuple
# b = {23, 45, 6, 7, 232, 345}
# y = tuple(b)
# print(y, type(y))
# ..........................................................
# READ
# Index
# x = (2, 3, 4, 5, 6, 1, 23, 34, 56)
# print(x[1])
# print(x[-1])

# Slicing
# print(x[4::-1])
# print(x[5::1])
# print(x[-4::1])

# Loops
# for i in x:
#     print(i)

# for i in range(len(x)):
#     print(i, x[i])
# ..................................................
# x = (2, 3, 5, 6, 7, 8, 9, 10)
# # print(x[-3])
# # print(x[5:0:-1])
# print(x[-3:-7:-1])
# ..................................................................
# Merging the tuple
# x = (23, 45, 6, 7)
# y = (45, 78, 90, 34)
# t = (45, 23, 1, 2, 3, 4)

# z = x + y + t
# print(z, type(z))

# ..............................
# PROBLEMS............
# nested = (1, 2, (3, 4), [5, 6], {23, 45, 190})
# nested[3].append(7)
# print(nested)
# nested[3].extend([9, 34, 23, 12])
# print(nested)
#
# nested[4].add(0)
# print(nested)
