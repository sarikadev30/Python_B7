# File Handling

# Reading A file
# with open("data.txt","r") as f:
#     content=f.read()
#     print(content)
# .........................................................


# Writing into a file

# with open("action.txt","w") as f:
#     f.write("Hi! .. I am writing into a file.")

# .........................................................
# Appending in a file

# with open("action.txt",'a') as f:
#     f.write("Bye.....................")

# .........................................................
# File mode => r+ => No file creation is possible

# with open("data.txt","r+") as f:
#     print(f.tell())
#     print(f.read())
#     print(f.tell())
#     f.write("Hi! I am Back.")
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())
#     f.write("Updates done")

# ..........................................................

# w+ and a+ mode (readline , readlines)