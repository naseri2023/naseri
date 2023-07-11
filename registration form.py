import mysql.connector as mysql
from tkinter import *
from tkinter import messagebox

form=Tk()
form.geometry("600x300")
form.title("Registration Form")
form.config(bg="whitesmoke")

def open():
    connection = mysql.connect(host="localhost", database="new1", user="root")
    cursor = connection.cursor()
    cursor.execute('select * from new_table')
    result = cursor.fetchall()
    for row in result:
        new_row=(row[0],row[1],row[2])
        text_box.insert(0,new_row)
    connection.commit()
    cursor.close()

def register():
    if entry_id.get()=="":
        var = messagebox.showinfo("Registration Dialog", "Please complete the form!")
    elif entry_avg.get()=="":
        var = messagebox.showinfo("Registration Dialog", "Please complete the form!")
    elif entry_name.get() == "":
        var = messagebox.showinfo("Registration Dialog", "Please complete the form!")
    else:
        connection = mysql.connect(host="localhost", database="new1", user="root")
        mysql_insert = 'insert into new_table(id,name,avg)values(%s,%s,%s)'
        record = (entry_id.get(), entry_name.get(), entry_avg.get())
        cursor = connection.cursor()
        cursor.execute(mysql_insert, record)
        connection.commit()
        cursor.close()
        var = messagebox.showinfo("Registration Dialog", "Registered successfully")
    entry_id.delete(0,END)
    entry_avg.delete(0,END)
    entry_name.delete(0,END)

def delete_user():
    # entry_id.insert(0, id_split)
    # entry_name.insert(0, name_split)
    # entry_avg.insert(0, avg_split)
    record = text_box.get(ANCHOR)
    id_split = record[0]
    entry_id.insert(0,id_split)
    name_split=record[1]
    entry_name.insert(0,name_split)
    avg_split=record[2]
    entry_avg.insert(0,avg_split)
    connection = mysql.connect(host="localhost", database="new1", user="root")
    cursor = connection.cursor()
    mysql_delete = 'delete from new_table where id=%s,name=%s,avg=%s'
    record1=(int(entry_id.get()),str(entry_name.get()),float(entry_avg.get()))
    cursor.execute(mysql_delete,record1)
    connection.commit()
    cursor.close()
    var = messagebox.showinfo("Registration Dialog", "Deleted successfully")

    entry_id.delete(0, END)
    entry_avg.delete(0, END)
    entry_name.delete(0, END)

def update_user():
    connection = mysql.connect(host="localhost", database="new1", user="root")
    cursor = connection.cursor()
    mysql_update='update new_table set id=%s where id=103'
    record = [entry_id.get()]
    cursor.execute(mysql_update, record)
    connection.commit()
    cursor.close()
    var = messagebox.showinfo("Registration Dialog", "Updated successfully")
    entry_id.delete(0,END)
    entry_avg.delete(0,END)
    entry_name.delete(0,END)

def exit_user():
    if not messagebox.askyesno("Exit Dialog", "Are you sure?"):
        messagebox.showinfo("", "Welcome Back")
    else:
        exit()

def close_form():
    if messagebox.askyesno("Exit Dialog", "Are you sure?"):
        exit()

form.protocol("WM_DELETE_WINDOW",close_form)

def id(event):
    entry_id.config(bg='light cyan')

def id2(event):
    entry_id.config(bg="white")

def id3(event):
    entry_avg.config(bg='light cyan')

def id4(event):
    entry_avg.config(bg='white')

def id5(event):
    entry_name.config(bg='light cyan')

def id6(event):
    entry_name.config(bg='white')

def btn1(event):
    btn_register.config(bg='light cyan')

def btn2(event):
    btn_register.config(bg='white')

def btn3(event):
    btn_exit.config(bg='light cyan')

def btn4(event):
    btn_exit.config(bg='white')

def btn5(event):
    btn_delete.config(bg='light cyan')

def btn6(event):
    btn_delete.config(bg='white')

def btn7(event):
    btn_update.config(bg='light cyan')

def btn8(event):
    btn_update.config(bg='white')

label_id=Label(text="Student ID       ", bg="whitesmoke",foreground="black",anchor="w",justify=LEFT,font=("calibri",12))
label_id.place(relx=0.1,rely=0.1,anchor="c")

entry_id=Entry(foreground="black",bg="white",borderwidth=2,width=30)
entry_id.place(relx=0.4,rely=0.1,anchor="c")
entry_id.bind("<Enter>",id)
entry_id.bind("<Leave>",id2)

label_name=Label(text="Student Name", bg="whitesmoke",foreground="black",anchor="w",justify=LEFT,font=("calibri",12))
label_name.place(relx=0.1,rely=0.4,anchor="c")

entry_name=Entry(foreground="black",bg="white",borderwidth=2,width=30)
entry_name.place(relx=0.4,rely=0.4,anchor="c")
entry_name.bind("<Enter>",id5)
entry_name.bind("<Leave>",id6)

label_avg=Label(text="   Student Average", bg="whitesmoke",foreground="black",anchor="w",justify=LEFT,font=("calibri",12))
label_avg.place(relx=0.1,rely=0.7,anchor="c")

entry_avg=Entry(foreground="black",bg="white",borderwidth=2,width=30)
entry_avg.place(relx=0.4,rely=0.7,anchor="c")
entry_avg.bind("<Enter>",id3)
entry_avg.bind("<Leave>",id4)

btn_register=Button(text="REGISTER",foreground="black",bg="white",relief="ridge" ,padx=20,pady=10,borderwidth=1,command=register)
btn_register.place(relx=0.67,rely=0.1,anchor="c")
btn_register.bind("<Enter>",btn1)
btn_register.bind("<Leave>",btn2)

btn_delete=Button(text="DELETE",foreground="black",bg="white",padx=25,pady=10,borderwidth=1,command=delete_user,relief="ridge")
btn_delete.place(relx=0.67,rely=0.3,anchor="c")
btn_delete.bind("<Enter>",btn5)
btn_delete.bind("<Leave>",btn6)

btn_update=Button(text="UPDATE",foreground="black",bg="white",padx=22,pady=10,borderwidth=1,command=update_user,relief="ridge")
btn_update.place(relx=0.67,rely=0.5,anchor="c")
btn_update.bind("<Enter>",btn7)
btn_update.bind("<Leave>",btn8)

btn_exit=Button(text=" EXIT",foreground="black",bg="white",padx=33,pady=10,borderwidth=1,command=exit_user,relief="ridge")
btn_exit.place(relx=0.67,rely=0.7,anchor="c")
btn_exit.bind("<Enter>",btn3)
btn_exit.bind("<Leave>",btn4)

text_box=Listbox(width=20,height=16,borderwidth=4)
text_box.place(relx=0.89,rely=0.46,anchor="c")

open()
form.mainloop()