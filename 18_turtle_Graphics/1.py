from turtle import Turtle, Screen

timmy=Turtle()
timmy.shape("turtle")
timmy.color("red")
i=0
while i<=3:
    timmy.forward(200)
    timmy.right(90)
    i+=1

screen=Screen()
screen.exitonclick()