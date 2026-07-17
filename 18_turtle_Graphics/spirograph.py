from turtle import Turtle ,Screen ,colormode
from random import randint
timmy=Turtle()
timmy.circle(100)
timmy.speed("fastest")

t=colormode(255)
def random_color():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    color=(r,g,b)   
    return color

#it also creates a spirograph but without changing heading instead we change position and an inside circle is made
# for i in range(100):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.right(10)
#     timmy.forward(5)

for i in range(100):
    timmy.color(random_color())
    timmy.circle(100)
    current_heading=timmy.heading()
    new_heading=timmy.setheading(current_heading+10)
   


screen=Screen()
screen.exitonclick()