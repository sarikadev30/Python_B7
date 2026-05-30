# Functions


# def fun(x, y):
#     print(x + y)


# fun(5, 4)

# types of functions

# Default argument Function


# def fun(x, y, z=8):
#     print(x + y + z)


# # fun(4)
# fun(4, 8)
# .........................................................
# Variable Length Argumented Functions


# def addValues(*y):
#     print(y)
#     print(sum(y))


# addValues(2)
# addValues(2, 3)
# addValues(2, 4, 5, 6)

# ..........................................................
# Keyworded argument function


# def fun(name, age, salary, department):
#     print("name: ", name)
#     print("age: ", age)
#     print("salary: ", salary)
#     print("department: ", department)


# # fun("Sam", 23, 23000, "IT")

# fun(age=23, name="Sam", department="IT", salary=23000)


# fun("Sam", 23, department="IT", salary=23000)
# ..........................................................
# print and return


# def fun(w, x):
#     print(w + x)


# fun(3, 4)


# def fun2(w, x):
#     return w + x


# c = fun2(4, 5)
# print(c)

# .................................................
# FACTORIAL 5! => 5*4*3*2*1 =>120
# 0! => 1
# 1! => 1


# def factorial(n):
#     fact = 1
#     for i in range(n, 0, -1):
#         fact *= i

#     # print(fact)
#     return fact


# # factorial(5)


# u = factorial(5)
# print(u)
# ...........................................................
# fibonacci series
# 0 1 1 2 3 5 8 13..........
# a b c
#   a b c
def fibonacci(n):
    a = 0
    b = 1
    res = []
    for i in range(n):
        res.append(a)
        c = a + b
        a = b
        b = c
    return res


ans = fibonacci(4)
print(ans)
