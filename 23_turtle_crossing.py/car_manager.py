from turtle import Turtle
from random import randint,choice
car_color=["red","blue","yellow","green","pink","purple"]
move_distance=5
move_increment=10

class Car_manager(Turtle):
    def __init__(self):
        self.all_cars=[]
        self.car_speed=move_distance

    def create_car(self):
        random_chnace=randint(1,5)
        if random_chnace==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(choice(car_color))
            random_y=randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed +=move_increment  
    