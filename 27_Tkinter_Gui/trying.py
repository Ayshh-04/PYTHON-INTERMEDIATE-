from tkinter import *

def button_clicked():
    my_label.config(text=input.get())

window=Tk()
window.title("my first window")
window.minsize(height=300,width=500)
window.config(padx=20,pady=20)

#label
my_label=Label(text="this is an label",font=("arial",24,"bold"))
# my_label.pack()
#  #this paks and shows the label on screen (important)
# you can change labels or configurate vvalue of label
my_label.config(text="new text") 

# my_label.place(x=0,y=0)        #its to precise and hard to imagine

my_label.grid(column=0,row=0)
#button
button=Button(text="click me",command=button_clicked)
# button.pack()
button.grid(column=0,row=1)
#entry
input=Entry(width="10")
# input.pack()
print(input.get())
input.grid(column=3,row=2)
window.mainloop()



#we commented out pack just cause we cant use grid and pack togeether choose one

# # astrick operator -*args and is use for unlimited arhument and treats it as tuple
# def add(*args):
#     sum=0
#     for n in args:
#         sum +=n
#     print(sum)
# add(5,3,7,5,8,4,2,5,7)

# # double astrick - **kwargs is use for unlimited labeled argument and treats as dictionary storees in key value pair and access like that
# def calculations(**kwargs):
#     # print(kwargs)
#     for key,value in kwargs.items():
#         print(key)
#         print(value)
#     print(kwargs["name"])

# calculations(name="ayush",year="third")

#ARGUMENT IN CLASS CAN  BE PASSED LIKE THIS
# class car:
#     def __init__(self,**kw):
#         self.model=kw.get("model")
#         self.name=kw.get("name")

# my_car=car(model="nissan",name="GT-R")
# print(my_car.name)