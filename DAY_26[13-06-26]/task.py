# PYTHON EXCEPTIONS

# print("Hello World")

# x=5
# print(x+78)
# y=[1,2,3,4,5,6,7,8,9]

# print(y[9])

# ................................
# print(0/23)
# ZeroDivisionError : division by 0
# print(23/0)

# ValueError : 
# x=int(input("Enter a number: ")) 
# print(x)

# IndexError :
# y=[1,2,3,4,5,6,7,8,9]
# print(y[9])
# ..................................................

# try-except block
# print("Hello World.....")
# print("Hello World.....")
# print("Hello World.....")

# try:
#     value=int(input("Enter a number: ")) 
#     ans=50/value
#     print(ans)
# except ZeroDivisionError:
#     print("Number you entered should not be zero....")

# print("Hello World.....")
# print("Hello World.....")
# print("Hello World.....")
# ................................................................
# multiple except block

# try:
#     value=int(input("Enter a number: ")) 
#     ans=50/value
#     print(ans)
# except ZeroDivisionError:
#     print("Number you entered should not be zero....")
# except ValueError:
#     print("Enter a number not a word (string)")
# ...............................................................
# Catching multiple exceptions together

# try:
#     value=int(input("Enter a number: ")) 
#     ans=50/value
#     print(ans)
# except (ValueError, ZeroDivisionError) as e:
#     print("error : ", e)
# ......................................................................