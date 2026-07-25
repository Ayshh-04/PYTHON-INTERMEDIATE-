#absolute method 
# with open("D:/001. PYTHON/FILES_LEARNING/new_my_file.txt",mode="r") as file:
#     content=file.read()
#     print(content)

# relative meethod ../../
with open("../FILES_LEARNING/new_my_file.txt", "r") as file:
    print(file.read())
