# s = [1, 2, 3, 45, 67, 89]
# fetch
# print(s[4])
# add at particular location
# s.insert(5, 90)
# print(s)

# slicing => taking some part of the list
# deleting
# looping
# for i in range(len(s)):
#     print(i, s[i])

# ......................................................................
# SETS
# CRUD (CREATE READ UPDATE DELETE)

# CREATE
# s = {1, 2, 3, 4, 5, 6, 78}
# print(s, type(s))

# y = set((2, 3, 45, 6, 78))
# print(y, type(y))

# print(s[4]) indexing not possible
# print(s[2:5:1]) slicing is also not possible
# .....................................................
# READ
# for i in s:
#     print(i)
# .....................................................
# UPDATE
# Add
# add a single element => add()
# s.add(89)
# print(s)
# add a list to the set => update()
# s.update([2, 3, 4, 5, 6, 7, 8, 90])
# print(s)

# Replace  X => not possible
# .....................................................
# DELETE

# remove() => if value is not present , remove will raise an error
# s.remove(78)
# s.remove(99)
# print(s)
# .......................
# discard() =>  if value is not there, discard will not raise an error
# s.discard(78)
# print(s)
# s.discard(99)
# print(s)
# ......................
# clear() => removes all the elements
# s.clear()
# print(s)
# ......................
# pop() => removes the first element in that scenario
# print(s.pop())
# print(s)
# ...........................................................
# SEARCHING
# print(69 in s)
# print(69 not in s)
# ......................................................................
# Problems
# letters = set("mississippi")

# print(letters, len(letters))
# letters.pop()
# print(letters)
# ..........................................................................................
