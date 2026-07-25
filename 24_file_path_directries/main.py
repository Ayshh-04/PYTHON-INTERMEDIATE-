# file = open("my_file.txt")
# content=file.read()
# print(content)
# file.close()   open close file manually

# with open("my_file.txt") as file:
#     content=file.read()
#     print(content)     #closes after use due to with keyword

#writing to a file
# with open("my_file.txt",mode="w") as file:
#     file.write("new text")

#append adds doesntdelete previous text
# with open("my_file.txt",mode="a") as file:
#     file.write("new text appended.")

#new file created if new file name added 
# with open("new_my_file.txt",mode="a") as file:
#     file.write("new text appended in new file.")

#to check your file path 
# import os
# print("Current working directory:", os.getcwd())
# file = open("my_file.txt")
