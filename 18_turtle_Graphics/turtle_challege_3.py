from turtle import Turtle, Screen ,pen

timmy=Turtle()

#draw triangle
for i in range(3):
    timmy.forward(100)
    timmy.right(120)
#draw square
for i in range(4):
    timmy.forward(100)
    timmy.right(90)

#draw pentagon
for i in range(5):
    timmy.forward(100)
    timmy.right(72)


#draw hexagon
for i in range(6):
    timmy.forward(100)
    timmy.right(60)
    
#draw heptagon
for i in range(7):
    timmy.forward(100)
    timmy.right(51.42)

#draw octagone
for i in range(8):
    timmy.forward(100)
    timmy.right(45)

#draw nanogone
for i in range(9):
    timmy.forward(100)
    timmy.right(40)

#draw decagon
for i in range(10):
    timmy.forward(100)
    timmy.right(36)


screen=Screen()
screen.exitonclick()