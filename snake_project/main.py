from turtle import Screen
import time 
from snake_function import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # FOOD COLLISION
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()   
        scoreboard.increase_score()

    # WALL COLLISION
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.snake_reset()

    # TAIL COLLISION
    for seg in snake.segments[1:]:  # skip head
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.snake_reset()
            
    #slcing is a way through which we can access particular data in list dictionaries
    #segmens[2:5] #this take data from this point and [2:]till end from zero
    #[:5]5 index ke pehle ke le lega #[2:5:7]skips 5[::2]beginning till end skip 2nd one
    #[::-1] reverse the list 
    #slicing also work on tuple(2:5) 

screen.exitonclick()