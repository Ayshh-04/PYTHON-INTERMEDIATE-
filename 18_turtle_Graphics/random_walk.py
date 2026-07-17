from turtle import Turtle as t #we can set module name using as
from turtle import Screen #to display 
from random import choice
timmy=t()
timmy.pensize(15) #can select pen thickness
colour=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction=[0,180,90,270] 
timmy.speed("fastest")

for i in range(200):
    timmy.color(choice(colour))
    timmy.forward(30)
    timmy.setheading(choice(direction))

screen=Screen()
screen.exitonclick()