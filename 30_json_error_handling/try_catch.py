#EXCEPTIONAL HANDLING -TRY: except: else: finally:

# #file not found
# with open("file.txt") as file:
#     file.read()
# #key error
# a_dict=["key":"value"]
# value=a_dict["non_existing_key"]
# #index error
# a=["ayush","renu","bhumi"] 
# print(a[3])
# #type error
# text="abc"
# print(text+5)


#FOUR MOST IMPORTANT KEYWORDS IN ERROR HANDLING AND EXCEPTION CASES
# and raise to raise your own error

# try:
#     file=open("file.txt")
#     a_dict={"key":"value"}
#     value=a_dict["non_existing_key"]
#     print(value)
    
# except FileNotFoundError: #never use bae except otherwise it will also remove other error always specify
#     file=open("file.txt","w")
#     file.write("something")

# except KeyError as error_message:
#     print(f"the {error_message} was not found in dictionary")

# else: #if no exceptions are catched then
#     content=file.read()
#     print(content)

# finally:
#     raise TypeError("this is the error i made")



# #raising error by our own 
# height=float(input("height in meters: "))
# weight=float(input("weight in kilo's: "))

# if height>3:
#     raise ValueError("Human Height cannot be greater than 3 meter")

# bmi=weight/height**2
# print(f"your bmi is {bmi}.")
