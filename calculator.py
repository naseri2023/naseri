from tkinter import *
form=Tk()

form.rowconfigure((0,1,2,3,4,5),weight=1)
form.columnconfigure((0,1,2,3,),weight=1)
window=Entry(width=35,borderwidth=5)
window.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def btn_add():
    global first_num
    global math
    first_num=int(window.get())
    math="add"
    window.insert(0,first_num)
    window.delete(0, END)

def btn_sub():
    global first_num
    global math
    first_num = int(window.get())
    math = "min"
    window.insert(0, first_num)
    window.delete(0, END)

def btn_mul():
    global first_num
    global math
    first_num = int(window.get())
    math = "mul"
    window.insert(0, first_num)
    window.delete(0, END)

def btn_div():
    global first_num
    global math
    first_num = int(window.get())
    math = "div"
    window.insert(0, first_num)
    window.delete(0, END)

def btn_equ():
    second_num=int(window.get())
    window.delete(0, END)
    if math=="add":
        answer=first_num+second_num
        window.insert(0,answer)

    if math=="min":
        answer=first_num-second_num
        window.insert(0,answer)

    if math=="mul":
        answer=first_num*second_num
        window.insert(0,answer)

    if math=="div":
        answer=(first_num)/(second_num)
        window.insert(0,answer)
        
def btn_clr():
    window.delete(0, END)

def nums(number):
    added=window.get()
    window.delete(0,END)
    window.insert(0, str(added)+str(number))

form.title("Calculator")

btn_1=Button(text="1",padx=40,pady=20,command=lambda :nums(1))
btn_2=Button(text="2",padx=40,pady=20,command=lambda :nums(2))
btn_3=Button(text="3",padx=40,pady=20,command=lambda :nums(3))

btn_4=Button(text="4",padx=40,pady=20,command=lambda :nums(4))
btn_5=Button(text="5",padx=40,pady=20,command=lambda :nums(5))
btn_6=Button(text="6",padx=40,pady=20,command=lambda :nums(6))

btn_7=Button(text="7",padx=40,pady=20,command=lambda :nums(7))
btn_8=Button(text="8",padx=40,pady=20,command=lambda :nums(8))
btn_9=Button(text="9",padx=40,pady=20,command=lambda :nums(9))

btn_0=Button(text="0",padx=40,pady=20,command=lambda :nums(0))
btn_addition=Button(text="+",padx=86,pady=20,command=btn_add)
btn_subtraction=Button(text="-",padx=40,pady=20,command=btn_sub)

btn_multiplication=Button(text="*",padx=40,pady=20,command=btn_mul)
btn_division=Button(text="/",padx=40,pady=20,command=btn_div)

btn_equal=Button(text="=",padx=39,pady=20,command=btn_equ)
btn_clear=Button(text="clear",padx=76,pady=20,command=btn_clr)

btn_1.grid(row=1,column=0)
btn_2.grid(row=1,column=1)
btn_3.grid(row=1,column=2)

btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)

btn_7.grid(row=3,column=0)
btn_8.grid(row=3,column=1)
btn_9.grid(row=3,column=2)

btn_0.grid(row=4,column=0)
btn_equal.grid(row=5,column=0)

btn_addition.grid(row=4,column=1,columnspan=2)
btn_clear.grid(row=5,column=1,columnspan=2)

btn_subtraction.grid(row=6,column=0)
btn_multiplication.grid(row=6,column=1)
btn_division.grid(row=6,column=2)

form.mainloop()