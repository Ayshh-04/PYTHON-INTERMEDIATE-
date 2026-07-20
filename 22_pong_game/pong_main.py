from turtle import Screen
from paddle import Paddle
from pong_ball import Ball
from pong_scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PING_PONG")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))

ball=Ball()
scorboard=Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.y_bounce()
        
    if ball.distance(r_paddle)<50 and ball.xcor()>350 or ball.distance(l_paddle)<50 and ball.xcor()<-350:
        ball.x_bounce()
    
    if ball.xcor()>380:
        ball.reset_postion()
        scorboard.l_point()
    
    if ball.xcor()<-380:
        ball.reset_postion()
        scorboard.r_point()
    
    if scorboard.l_score ==5 or scorboard.l_score ==5:
        game_is_on=False
        

screen.exitonclick()