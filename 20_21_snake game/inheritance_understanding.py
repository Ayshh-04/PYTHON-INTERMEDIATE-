#class inheritance oop concept classes can inherit from another classs like attribute methods and also how python allow to slice dictionaries and lists
#we can inherit attributes and methods(behaviour)
class Animal():
    def __init__(self):
        self.num_eyes=2  
    def breathe(self):
        print("inhale,exhale")

class Fish(Animal): #here we are announcing our super class 
    def __init__(self): #we are initialising all the attributes and methods from animal class to fish class
        super().__init__() #thismostly initialise the function of constructor part only 

    def breathe(self):
        super().breathe() #like this we can access and modify function and function can be used in differe function
        print("breathing under water") # it brings all what we were doing there here

    def swim(self):
        print("swimming") #simple function

nemo=Fish() #creating object from child class
nemo.swim()
nemo.breathe()#this is an inherited method ofn fish class from animal class
print(nemo.num_eyes)#this is attribute it gets iniatited from super().__init__()