# print numbers from 1 to 10 using while loop

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# ...............................................................
#  Print the sum of numbers from 1 to 4
# i = 1
# sum = 0
# while i <= 4:  # 1 2 3 4
#     sum += i  # sum=sum+i
#     i += 1

# print(sum)

# DRY RUN
# i=1 sum=0
# i=1 1<=4 => T => sum=0+1=1 => i=1+1=2
# i=2 2<=4 => T => sum=1+2=3 => i=2+1=3
# i=3 3<=4 => T => sum=3+3=6 => i=3+1=4
# i=4 4<=4 => T => sum=6+4=10 => i=4+1=5
# i=5 5<=4 => F => ENDS........................
# 10
# .................................................................

#  Print the product of numbers from 1 to 4

# .......................................................................
# WHILE LOOP WITH BREAK
# Break => stops the execution

# print("Start")
# i = 1
# while i < 5:
#     print(i)
#     if i == 3:
#         break

#     i += 1
# print("End")

# ......................................................................
# WHILE LOOP WITH CONTINUE
# continue => skips the execution

# print("Start")
# i = 1
# while i < 5:
#     i += 1  # 2 3 4 5
#     if i == 3:
#         continue
#     print(i)

# print("End")
# ........................................................................
# FOR LOOP

#  for i in sequence:
# print(i)

# range(start, end, step)   start = 0  end=3  (end-1)=2   step=1

# for i in range(0, 3, 1):  # 0 1 2
#     print(i)

#  step => default = 1
# for i in range(0, 3):  # 0 1 2
#     print(i)

# start => default = 0
# for i in range(3):  # 0 1 2
#     print(i)


# for i in range(1, 3):
#     print(i)

# for i in range(3, 0, -1):  # 3  2  1
#     print(i)

# for i in range(0, 5, 2):  # 0 2 4
#     print(i)

# for i in range(0, 5, 3):  # 0 3
#     print(i)

# for i in range(6, 0, -2):  #
#     print(i)


# for i in range(10, -1, -1):
#     print(i)
# .....................................................................
# HOMEWORK
# sum using for loop
# product using the for loop
# average using for loop

# ......................................................................
