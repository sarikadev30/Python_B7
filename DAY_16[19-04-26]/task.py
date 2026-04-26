# PROBLEM 1 **Perform the following tasks :**
# 1. **Create list of superheroes**
# 2. **push 4 superheroes in the List**
# 3. **Print the List**

# superheroes = []
# superheroes.append("Ironman")
# # print(superheroes)
# superheroes.append("Batman")
# # print(superheroes)
# superheroes.extend(["Thanos", "Spiderman"])
# print(superheroes)

# ........................................................................................
# DELETE

# pop(index) => will delete value on the basis of index

# z = [2, 10, 3, 4, 10, 1, 6, 10, 7, 10, 8, 9, 10, 23, 10]

# z.pop(2)
# print(z)
# z.pop()  # if index is not given , it will remove last element
# print(z)
# .......................................................................
# remove(value)  => will delete the value on the basis of value only
# z.remove(2)
# print(z)
# z.remove(10)
# print(z)

# .......................................................................
# PROBLEM
# stationary = []
# stationary.extend(["pen", "pencil", "notebooks", "marker", "Eraser", "Sharpner"])
# print(stationary)
# stationary.remove("marker")
# print(stationary)
# stationary.pop(2)
# print(stationary)
# stationary.pop()
# print(stationary)
# ..........................................................................................
# movies = ["bahubali", "Spider-Man", "Iron Man", "Superman"]
# for i in range(len(movies)):
#     if i == 3:
#         break
#     print(movies[i])
# ..........................................................................................

# INBUILT FUNCTIONS

# z = [1, 8, 9, 10, 2, 3, 4, 5, 6, 7, 1]

# # SUM
# x = sum(z)
# print(x)
# # MAX
# y = max(z)
# print(y)
# # MIN
# m = min(z)
# print(m)
# # LENGTH OF THE LIST
# c = len(z)
# print(c)
# # .index()
# # a = z.index(10)
# a = z.index(1)
# print(a)
