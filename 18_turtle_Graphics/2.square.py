from turtle import Turtle, Screen ,pen

timmy=Turtle()
# timmy.shape("turtle")
# timmy.color("red")

#draw square
# for i in range(4):
#     timmy.forward(200)
#     timmy.right(90)


# dashed line
for i in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


screen=Screen()
screen.exitonclick()