from time import *
from tkinter import *

def Time():
    Time1=strftime("%I:%M:%S\t%p\n\nToday is %A")
    label.config(text=Time1,font=("Arial",20))
    label.after(1000,Time)

form=Tk()

form.geometry("500x150")
label=Label()
label.place(x=140,y=20)
Time()
form.mainloop()