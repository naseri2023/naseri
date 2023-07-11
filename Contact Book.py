from tkinter import *
import os
import webbrowser
from tkinter import messagebox
from tkinter import ttk

root=Tk()
root.title("Contact Book")
root.geometry("600x300")
root.config(bg="light blue")

def exit_root():
    var=messagebox.askyesno("Exit Dialog","Are you sure?")
    if not var:
        messagebox.showinfo("","Welcome Back")
    else:
        exit()

def add_contact():
    text=" "+name_entry.get()+": "+phone_entry.get()
    name_entry.delete(0,END)
    phone_entry.delete(0,END)
    text_box.insert(END,text)

def delete_contact():
    text_box.delete(ANCHOR)

def save_contact():
    with open("C:\\Users\\Webhouse\\Documents\\python.txt","w") as f:
        new1=text_box.get(0,END)
        for items in new1:
            if items.endswith=="/n":
                f.write(items)
            else:
                f.write(items+"\n")

def open_listbox():
    with open("C:\\Users\\Webhouse\\Documents\\python.txt","r") as f:
        for lines in f:
            text_box.insert(0,lines)

def open_file():
    webbrowser.open("C:\\Users\\Webhouse\\Documents")

def edit_contact():
    new_text=text_box.get(ANCHOR)
    new_split=new_text.split(": ")
    name_split=new_split[0]
    inserted=name_entry.insert(0,name_split)
    phone_split = new_split[1]
    inserted1 = phone_entry.insert(0, phone_split)
    text_box.delete(ANCHOR)

def photo():
    canvas = Canvas(height=700, width=700)
    canvas.create_image(10, 10, image=img, anchor=NW)
    canvas.pack()
img = PhotoImage(file="red-rose-on-black-background-649x1024.gif")
name_label=Label(text="Name Contact",foreground="black",bg="light blue",anchor="w",justify=LEFT,font=("calibri",12))
name_label.place(relx=0.1,rely=0.1,anchor="c")

name_entry=Entry(foreground="black",bg="white",borderwidth=2,width=30)
name_entry.place(relx=0.4,rely=0.1,anchor="c")

phone_label=Label(text="Phone Contact",foreground="black",bg="light blue",anchor="w",justify=LEFT,font=("calibri",12))
phone_label.place(relx=0.1,rely=0.2,anchor="c")

phone_entry=Entry(foreground="black",bg="white",borderwidth=2,width=30)
phone_entry.place(relx=0.4,rely=0.2,anchor="c")

add_btn=Button(text="Add Contact",foreground="black",bg="light yellow",padx=124,borderwidth=3,command=add_contact)
add_btn.place(relx=0.29,rely=0.35,anchor="c")

save_btn=Button(text="Save Contact",foreground="black",bg="light yellow",borderwidth=3,padx=36,command=save_contact)
save_btn.place(relx=0.14,rely=0.50,anchor="c")

copy_btn=Button(text="   Edit Phone Number",foreground="black",bg="light yellow",borderwidth=3,padx=14,command=edit_contact)
copy_btn.place(relx=0.14,rely=0.65,anchor="c")

del_btn=Button(text="   Delete Contact",foreground="black",bg="light yellow",borderwidth=3,padx=30,command=delete_contact)
del_btn.place(relx=0.43,rely=0.65,anchor="c")

open_saved_btn=Button(text=" Open Saved File",foreground="black",bg="light yellow",borderwidth=3,padx=27,command=open_file)
open_saved_btn.place(relx=0.14,rely=0.78,anchor="c")

exit_btn=Button(text="Exit",foreground="black",bg="light yellow",borderwidth=3,padx=64,command=exit_root)
exit_btn.place(relx=0.43,rely=0.78,anchor="c")

photo_btn=Button(text=" Contact Image",foreground="black",bg="light yellow",borderwidth=3,padx=32,command=photo)
photo_btn.place(relx=0.43,rely=0.50,anchor="c")

text_box=Listbox(width=35,height=15,borderwidth=3)
text_box.place(relx=0.78,rely=0.46,anchor="c")

open_listbox()
root.mainloop()