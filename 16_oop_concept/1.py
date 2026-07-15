#class and object

#(object)car=(class)carblueprint()

#import turtle 
#timmy=turtle.Turtle() #aese bhi likh skte the turtle already ek defined class h 

from turtle import Turtle ,Screen   #this all here is in this turtle module predefined





# brand new object-turtle and and print trtle object
timmy=Turtle()
timmy.shape("turtle")
#https://docs.python.org/3/library/turtle.html         documentation for this library 
print(timmy)
timmy.forward(100)
#we can move our turtle
my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
#car.speed
#object.attribute