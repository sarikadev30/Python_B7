# SCOPE of A Variable
# LOCAL => ENCLOSING => GLOBAL SCOPE => BUILT IN SCOPE


# Local Scope
def greet():
    message = "Hello"
    print(message)  # message is local to this function

# greet()
# print(message)   # Error: message is not defined
# .................................................................................
# Enclosing scope

# def outer():
#     msg = "Hello"     # local scope

#     def inner():
#         nonlocal msg
#         msg = "Hi"
#         print("Inner:", msg)

#     inner()

    
#     print("Outer:", msg)

# outer()

# msg="hello"=> "Hi"
# ..............................................................................
# Global Scope
# x = 10  # Global variable

# def print_x():
#     print(x)

# print_x()
# ..............................................................................
# Enclosing Scope
# def fun():  # x = 89
#     x = 89
#     print(x)    # 89

#     def innerFun():  # x=67
#         nonlocal x
#         x = 67
#         print(x)           # 67
#     innerFun()
#     print(x)               # 67 x =>89

# fun()

# 1     2 
# x     
# ..................................................................................
# built in scope

# print(len("python"))

# Local → Enclosing → Global → Built-in
# value =x

# .............................................................................................

# x = 100


# def change():
#     global x
#     print(x)
#     x = 200
#     print(x)


# change()
# print(x)
# ......................................................................................

# x = "global"


# def outer():
#     x = "outer"    # local variable for the outer function

#     def inner():
#         print("inner:", x)

#     print("outer:", x)
#     inner()
    


# outer()
# print("global", x)

# ...................................................................................

def func():
    print(x)


# func()  
x = 50
func()