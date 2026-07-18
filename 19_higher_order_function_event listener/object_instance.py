from turtle import Turtle,Screen
from random import randint

#starte is like color or doing something    instance is differt turtle t1,t2,t3 like this object=t1 and class =turtle()

is_race_on=False # for while loop continuing tuetle race providing random speed

screen=Screen()
screen.setup(width=500,height=400) #for understanding our race course
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")# top me tille likhna niche discription it num input bhi le skte
y_position=[-100,-50,0,50,100,150] # tarting point for turtles
colors=["red","orange","green","yellow","purple","blue"] #differentiating colors
all_turtle=[] # empty list to store created colors

for i in range (0,6): 
    turtle=Turtle(shape="turtle")
    turtle.penup() #we dont want line
    turtle.color(colors[i])
    turtle.goto(x=-240,y=y_position[i])
    all_turtle.append(turtle)
if user_bet:
    is_race_on=True # to avoid pre start of game 
while is_race_on :
    for t in all_turtle:
        if t.xcor()>230: # ending point of race
            is_race_on=False
            winning_color=t.pencolor() # pencolor turle ka color hota h line color ke ka 
            if winning_color==user_bet:
                print(f"you won !! {winning_color} is the winner")
            else:
                print(f"you lost !! {winning_color} is the winner")


        random_distance=randint(0,10) # 0 se 10 ke bichme random number dega jb tk x coordinate 230 nhi
        t.forward(random_distance)
        
screen.exitonclick()