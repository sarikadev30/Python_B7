x = [
    23,
    45,
    True,
    34.56,
    "sam",
    "Joe",
    "Monica",
    [23, 56, 78, 1, 2, 3, 4, [7, 90, 2, 3]],
    #    0    1   2   3  4  5  6    7
    #   -8   -7  -6  -5 -4 -3 -2   -1
    9,
    0,
]
# print(x, type(x))

# print(x[-2])
# print(x[-3][0])
# print(x[-6])
# print(x[4])
# print(x[7][-4])
# print(x[7][-1][-4])

# SLicing

# print(x[0:4:2])
# print(x[7:0:-2])

# .............................................................................................
# Problem:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#
#           -7        -6          -5        -4      -3     -2        -1
#             0      1          2          3       4       5         6

# print(thislist[-4:-1])  # [-4 : -1 ]
# print(thislist[:4])  # [0  : 4 : 1]
# print(thislist[2:5])  # [2: 5 :1]
# print(thislist[2:])  # [2 : 7 :  1]
# .............................................................................................

# UPDATE => Replace  Add

y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#    0   1  2  3  4  5  6  7  8

# REPLACING VALUE
# y[3] = 10
# print(y)

# y[8] = 23
# y[-1] = 23
# print(y)
# ......................................................................
# ADDING

# append(element) => Add an element to the list in the last


# y.append(32)
# print(y, len(y))
# ....................................................
# insert(index,element) => Add an element to the list at particular index

# y.insert(3, 50)
# print(y, len(y))

# .................................................................
# append(list) => Add the list as an element in the last
# y.append([2, 3, 4, 5, 6, 7])
# print(y)

# .................................................................
#  extend(list) => Add the list elemnents as individual

# y.extend([34, 67, 12, 90, 123, 45678, 0])
# print(y)

# .................................................................................................
# PROBLEM 1 **Perform the following tasks :**
# 1. **Create list of superheroes**
# 2. **push 4 superheroes in the List**
# 3. **Print the List**
