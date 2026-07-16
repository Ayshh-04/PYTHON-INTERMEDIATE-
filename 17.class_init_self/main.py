class User: #in class we tend to keep class with capital letter start
    pass
#user1 is an object and it calls out class User to attain its function and variables from class User 
user1=User()
#we can create attribute for every objectr just by 
user1.name="ayush"
print(user1.name)
#constructor or initialising the object

class Person:
    def __init__(self): #default constructor as it doesnot have any parameter then person1=self here it trear it as parameter
        print("ssup boy")
person1=Person()

class Human:
    def __init__(self,name,age): #now theres arguement constructor where we can se eparameters and call out as please
        self.name=name
        self.age=age
        self.friends=0 #instead of calling out in parameter if we can keep something constant here that doesnt need to included every time huser is created
c=Human("ayush",19)
print(c.name) #here c is treated as self there are three paramter though we passed 2 but 3rd is self=c which will always initiate 

class Car:
    def __init__(self,seat,cc):
        self.seat=seat
        self.cc=cc
    def start(self): #i ghave to pass self word if i have intiate the toyta i didnt last time it showd error as if we dont then it becomes car.start(toyota)
        print("car is started")#we can create funtion too an call it too 
    def shutting(self,speed):
        self.speed=speed
        print(f"stopping from {self.speed}km/hr to 0km/hr ")
    
toyota=Car(4,1000)
toyota.start()
toyota.shutting(40)
#we mostly used self in class only not in codes rarely i guess 
