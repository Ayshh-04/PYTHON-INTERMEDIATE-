#turtle event listner means program listening which keys is pressed on keyboard and doing job as per it

from turtle import Turtle ,Screen
timmy=Turtle()

screen=Screen()
screen.listen()    #now it will start listing now we have to bind a function 

#now in order to bind keystroke to an event we have to bind an key in our keyboard
#onkey(function(),(key eg-"space","a")) this binds function to a key then thats how that key works specific task
def move_forward():
    timmy.forward(50)

screen.onkey(key="space",fun=move_forward)
screen.exitonclick()

#higher order function is a fnxtion that can work with another function means
# def func_1(a,b,func_2): #we can use another function like def calculator(2,3,add): here add is function to add