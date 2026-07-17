#python tupple are t=(1,2,3) they are in order access using t[0] that is 1 
#tupple's are immutale , use tupple when need constant fix item
#we can make tuple mutable by putting it in list list=[t]

from turtle import Turtle as t 
from turtle import Screen  ,colormode
from random import choice,randint
timmy=t()
timmy.pensize(15)
t=colormode(255)
def random_color():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    color=(r,g,b)   
    return color
direction=[0,180,90,270] 
timmy.speed("fastest")

for i in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(choice(direction))

screen=Screen()
screen.exitonclick()