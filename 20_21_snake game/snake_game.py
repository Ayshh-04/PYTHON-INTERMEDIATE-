from turtle import Screen
import time 
from snake_function import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()#creating screen object
screen.setup(width=600,height=600) #setting height and width so we know co ordinate
screen.bgcolor("black") #background colour black
screen.title("snake Game") #use to title screen
screen.tracer(0)#It turns automatic screen updates ON/OFF this is done to stop goto positioning of 3 blocks

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:
    screen.update() #this breakers the tracer and show all movement at once skipping animation
    time.sleep(0.1) #using this Snake moves step by step → playable game
    snake.move()
    #detect collison of food and snake
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend_segment()
        scoreboard.increase_score()
    
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over_statement()
    
    for seg in snake.segments:
        if seg==snake.head:
            pass
        elif snake.head.distance(seg)<10:
            game_is_on=False
            scoreboard.game_over_statement() # tail collision 

screen.exitonclick()