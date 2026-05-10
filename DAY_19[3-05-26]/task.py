# Dictionary

# CRUD  => CREATE READ UPDATE DELETE

# CREATE

# 1. way

# d = {"name": "Sam", "age": 34, "city": "NY"}
# print(d, type(d))

# 2. way
# x = dict({"name": "Sam", "age": 34, "city": "NY"})
# print(x, type(x))

# ..................................................................
# READ

# print(x["name"])

# loop
# for key in x:
#     print(key, x[key])

# for key, value in x.items():
#     print(key, value)

# d = {
#     "name": ["Anny", "Bunny", "Danny", "Enav"],
#     "age": [25, 36, 22, 32],
#     "income": [90, 75, 80, 93],
# }

# print(d["name"][0], d["age"][0], d["income"][0])

# for i in d:
#     print(i, d[i][3])
# .......................................................

# x = {"name": "SAM", "age": 23, "city": "NY", "name": "Danny", "salary": 23}
# print(x)
# .............................................................................
# UPDATE

# x = dict({"name": "Sam", "age": 34, "city": "NY"})

# # Add
# x["salary"] = 230000
# print(x)

# # Replace
# x["name"] = "JOEY"
# print(x)

# ...........................................................................
# PROBLEM
# countries = ["India", "France", "Japan", "Canada"]
# capitals = ["New Delhi", "Paris", "Tokyo", "Ottawa"]

# # ccd={"India":"New Delhi","France":"Paris"....}

# ccd = {}
# for i in range(len(countries)):
#     ccd[countries[i]] = capitals[i]

# print(ccd)

# ...................................................................................
# DELETE
# x = dict({"name": "Sam", "city": "NY", "age": 34})

#  deleting a key value pair
# x.pop("name")
# print(x)

#  deleting the last key value pair
# x.popitem()
# print(x)

#  deleting all the key value pairs
# x.clear()
# print(x)

#  deleting the whole dictionary

# del x
# print(x)

# .......................................................................................
# Problem
# y = {}
# z = ()
# a = []
# print(y, z, a, type(y), type(z), type(a))


# o = {1, 2, 3, 4, 5}
# print(o, type(o))
# o.clear()
# print(o)
# ......................................................................................
