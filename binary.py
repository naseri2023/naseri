from tkinter import *

def binary():
    num=int(text1.get())
    base_num=int(text2.get())
    list_new=[]
    while num>0:
        pre_reminder=num%base_num
        reminder=str(pre_reminder)
        num=num//base_num
        list_new.append(reminder)
        joined="".join(list_new)
        reversed_reminder=joined[::-1]
    label.config(text="The binary number is : "+reversed_reminder)

form=Tk()
form.geometry("300x300")
form.title("Binary Numbers")
label_num=Label(text="Enter the number: ")
label_num.place(x=3,y=10)

label_base_num=Label(text="Enter the base number: ")
label_base_num.place(x=3,y=30)

text1=Entry()
text1.place(x=150,y=10)

text2=Entry()
text2.place(x=150,y=35)

btn_equal=Button(text="=",command=binary).place(x=150,y=80)

label=Label()
label.place(x=3,y=130)
form.mainloop()