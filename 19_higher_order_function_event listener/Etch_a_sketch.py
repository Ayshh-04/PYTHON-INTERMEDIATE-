from turtle import Turtle,Screen

timmy=Turtle()
screen=Screen()
screen.listen()

def move_forward():
    timmy.forward(10)

def right():
    new_heading=timmy.heading()+10
    timmy.setheading(new_heading)
    # timmy.right(10)

def left():
    new_heading=timmy.heading()-10
    timmy.setheading(new_heading)
    # timmy.left(10)

def move_backword():
    timmy.backward(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.onkey(key="w",fun=move_forward)
screen.onkey(key="d",fun=left)
screen.onkey(key="a",fun=right)
screen.onkey(key="s",fun=move_backword)
screen.onkey(key="c",fun=clear)


screen.exitonclick()