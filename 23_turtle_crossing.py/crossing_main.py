from turtle import Turtle,Screen
from player import Player
from crossing_scoreboard import Scoreboard
from car_manager import Car_manager
import time


screen=Screen()
screen.setup(height=600,width=600)
screen.tracer(0)


player=Player()
car_manager=Car_manager()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(player.move,"Up")
screen.title("turtle crossing road")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False
    
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.inc_level()

screen.exitonclick()