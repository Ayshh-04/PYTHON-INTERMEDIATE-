from tkinter import *
window=Tk()
window.title("Miles_to_KM_converter")
window.minsize(height=200,width=300)
window.config(padx=50,pady=50)


def calculate_km():
    get_mile=int(input_mile.get())
    calculation=round(get_mile*1.602)
    km_label.config(text=calculation)


mile_label=Label(text="enter mile")
mile_label.grid(column=0,row=0)

mile=Label(text="mile")
mile.grid(column=2,row=0)

input_mile=Entry(width=5)
input_mile.grid(column=1,row=0)

is_equal_to=Label(text="is equal to")
is_equal_to.grid(column=0,row=1)

km_label=Label(text="0")
km_label.grid(column=1,row=1)

km=Label(text="km")
km.grid(column=2,row=1)


button=Button(text="calculate",command=calculate_km)
button.grid(column=1,row=3)



window.mainloop()