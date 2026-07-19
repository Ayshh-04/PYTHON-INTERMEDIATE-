from turtle import Turtle

#these are constant 
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)] #the first three snake part position
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake():
    

    def __init__(self):
        #creating screen object
        self.segments=[] #to store snake length     
        self.create_snake()
        self.head=self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self,position):
        seg=Turtle(shape="square") #creating snake object loopin to create 60 pixel long snake
        seg.color("white")
        seg.penup() #to not show lines
        seg.goto(position) #position to make an  rectangle
        self.segments.append(seg)
    
    def extend(self):
        """adds a new segment to the end of the snake"""
        self.add_segment(self.segments[-1].position())  # get hold of the last segment in the list of segments# position is method give position of that segment and add segment to that


    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1): #(start=2(length of segment),0(end of segment),-1(its in reverse - for moving to previous one))
            new_x=self.segments[seg_num-1].xcor()  #previous ones co ordinate is give to following one
            new_y=self.segments[seg_num-1].ycor() 
            self.segments[seg_num].goto(new_x,new_y)  #seg_num will loop reverse 2 will go to -1 that is 1 co ordinate and this will go on and will help us even idf we make any turns as it isfollowing orevious one so any turn to snake will be change in  them too
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(270)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(0)
