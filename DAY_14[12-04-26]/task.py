# s = "hello"
# print(s)
# # strings are immutable
# s = "hfllo"
# # s[1] = "f"
# print(s)

# lst = [
#     1,
#     2,
#     3,
#     4,
#     "sam",
#     True,
# ]

# print(lst)
# lst[2] = "Danny"
# print(lst)
# # list is mutable (we can change the elements of the list)
# ......................................................................................
# LIST
# CREATE READ UPDATE DELETE (CRUD Operations)

# CREATE OPERATION
# 1. Way
# x = [1, 2, "Sam", True, 12.0, "Danny"]
# print(x, type(x))

# 2. Way
# y = list((1, 2, 9, 8, 6, 4, 34, 21))
# print(y, type(y))
# .......................................................
# READ OPERATION

x = [1, 2, "Sam", True, 12.0, "Danny"]
#    0  1   2      3     4      5         positive indexing
# Indexing
# print(x[5])
# length of the list => number of elements in a list
# print(len(x))

# y = [0, 2, 3, 4, 2, 4, 5, 7, 5, 4, 34, 67, 23, [5, 6, 7, 8, 9]]
#    0  1  2  3  4  5  6  7  8  9  10  11  12   13                         positive indexing starts from 0 and from left side

# print(len(y))  # 14
# print(y[8])
# print(y[13])
# [5, 6, 7, 8, 9]
#  0  1  2  3  4
# print(y[13][0])
# print(y[13][3])
# print(y[13][4])
# print(y[13][2])

# z = [9, 8, 7, 6, 4, 23, 90]
#    0  1  2  3  4   5   6
#   -7 -6 -5 -4 -3  -2  -1           Negative Indexing starts from -1 from right side

# print(len(z))  # 7
# print(z[5])  # 23
# print(z[-3])
# print(z[-6])

# y = [0, 2, 3, 4, 2, 4, 5, 7, 5, 4, 34, 67, 23, [5, 6, 7, 8, 9]]
# #                                  -4  -3  -2        -1

# print(y[-1])  # [5, 6, 7, 8, 9]
# #                0  1  2  3  4
# #               -5 -4 -3 -2 -1
# print(y[-1][2])

# print(y[-1][-3])
# print(y[-1][-5])
# ........................................

# K = [1, 2, 3, [1, 4, 5, 6, 7], "Sam", "Danny", True, 3.4]
# #    0  1  2      3             4       5        6    7
# print(len(K))
# print(K[5])
# print(K[-1])
# print(K[-5])
# print(K[-5][-1])
# print(K[-5][2])

# ..........................................
# LOOP
# z = [9, 8, 7, 6, 4, 23, 90]
# for i in z:
#     print(i)

# for i in range(len(z)):
#     print(i, z[i])

# ..........................................
# SLICING
z = [9, 8, 7, 6, 4, 23, 90]
#   0   1  2

# listName[startIndex:endIndex:step]
# print(z[0:3:1])
# start default = 0    step default = 1
# print(z[:4:])

# ..........................................................................
#
