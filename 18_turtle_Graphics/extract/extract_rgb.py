from turtle import Turtle,Screen,colormode
from random import choice
import colorgram
colours=colorgram.extract('image.jpg',10)


# rgb_color_list=[] # TO APPEND COLORS RGB TUPLE FORMATR

# for color in colours:
#     rgb_color_list.append(color.rgb) #this is one way but we need it more systematically to be able to use

# for color in colours: # using this we can extract color from image 
#     r=color.rgb.r (we are doing this to add this vriable in our tuple)
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_color_list.append(new_color)
    
# print(rgb_color_list)

timmy=Turtle()
timmy.speed("fastest")
timmy.penup() #remove line 
timmy.hideturtle() #hide cursor 
timmy.setheading(225) #use to set dot down so it can have screen to show complet animation
timmy.forward(300)
timmy.setheading(0)

colormode(255) #this tell us that it will use rgb value tuple 0 to 255
color_list=[(224, 223, 220), (167, 162, 155), (22, 23, 22), (222, 230, 223), (116, 97, 92), (234, 223, 226), (44, 107, 150), (153, 70, 90), (217, 226, 233), (218, 204, 129)]
number_dots=101
for dot_count in range(1,number_dots):
    timmy.dot(20,choice(color_list))
    timmy.forward(50)
    if dot_count % 10==0:
        timmy.setheading(90) #this is to move to another life after every 10 dots in line 
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

#to make such desing we need continously go back and forth for visualsation to make change accordingly

s=Screen()
s.exitonclick()