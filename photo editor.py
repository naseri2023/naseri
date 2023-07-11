from tkinter import *
import cv2
from tkinter import messagebox
from tkinter.filedialog import *
from PIL import Image, ImageTk, ImageGrab, ImageFilter, ImageDraw
import datetime

window = Tk()
window.iconbitmap('app_icon.ico')
window.title("Photo Edite")
window.geometry("862x519")
window.configure(bg="#3A7FF6")
w = 400;h = 400
size = (w, h)
def open_img():
    global im, resized, path, display, tkimage, imageFrame
    imageFrame = Frame(window)
    imageFrame.place(x=380, y=100)
    path = askopenfilename()
    im = Image.open(path)
    resized = im.resize(size, Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(resized)
    display = Label(imageFrame)
    display.imgtk = tkimage
    display.configure(image=tkimage)
    display.grid()

def save_img():
    resized.save(path)

def save_as():
    ts = datetime.datetime.now()
    filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
    resized.save(r'D:\\' + filename)
    if True:
        messagebox.showinfo("", "Saved Successfully!")
def resize_img():
    root=Toplevel(window)
    root.title('RESIZE')
    root.geometry('300x100')
    root.grab_set()

    def btn_resize():
        global display
        global imageFrame
        display.destroy()
        imageFrame.destroy()
        cv2.destroyAllWindows()
        resized = im.resize((int(entry_weight.get()),int(entry_height.get())),Image.ANTIALIAS)
        entry_height.delete(0, END)
        entry_weight.delete(0, END)
        tkimage1 = ImageTk.PhotoImage(resized)
        imageFrame1 = Frame(window)
        imageFrame1.place(x=380, y=100)
        display = Label(imageFrame1)
        display.imgtk = tkimage1
        display.configure(image=tkimage1)
        display.grid()
    label_weight=Label(root,text='Weight')
    label_weight.place(x=50,y=5)
    label_height=Label(root,text='height')
    label_height.place(x=50,y=30)
    entry_weight=Entry(root)
    entry_weight.place(x=100,y=5)
    entry_height=Entry(root)
    entry_height.place(x=100,y=30)
    btn_resized=Button(root,text='Resize Image',command=btn_resize)
    btn_resized.place(x=120,y=60)
    root.mainloop()

def black_white():
    gray = resized.convert('L')
    resi = gray.resize(size, Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(resi)
    imageFrame1 = Frame(window)
    imageFrame1.place(x=380, y=100)
    display =Label(imageFrame1)
    display.imgtk = tkimage1
    display.configure(image=tkimage1)
    display.grid()

def combine_img():
    path2 = askopenfilename()
    img2 = Image.open(path2)
    resized1 = im.resize(size, Image.ANTIALIAS)
    # im.paste(img2)
    tkimage1 = ImageTk.PhotoImage(resized1)
    imageFrame1 = Frame(window)
    imageFrame1.place(x=380, y=100)
    display = Label(imageFrame1)
    # display.imgtk = sum_img
    display.configure(image=img2.paste(im))
    display.place()

def rotate_img():
    img_rotate=resized.rotate(90)
    tkimage1 = ImageTk.PhotoImage(img_rotate)
    imageFrame1 = Frame(window)
    imageFrame1.place(x=380, y=100)
    display = Label(imageFrame1)
    display.imgtk = tkimage1
    display.configure(image=tkimage1)
    display.grid()

def blur_img():
    img_blur=resized.filter(ImageFilter.BLUR)
    tkimage1 = ImageTk.PhotoImage(img_blur)
    imageFrame1 = Frame(window)
    imageFrame1.place(x=380, y=100)
    display = Label(imageFrame1)
    display.imgtk = tkimage1
    display.configure(image=tkimage1)
    display.grid()


def gaussian_img():
    img_blur = resized.filter(ImageFilter.CONTOUR)
    tkimage1 = ImageTk.PhotoImage(img_blur)
    imageFrame1 = Frame(window)
    imageFrame1.place(x=380, y=100)
    display = Label(imageFrame1)
    display.imgtk = tkimage1
    display.configure(image=tkimage1)
    display.grid()

def EMBOSS_img():
    img_blur = resized.filter(ImageFilter.EMBOSS)
    tkimage1 = ImageTk.PhotoImage(img_blur)
    imageFrame1 = Frame(window)
    imageFrame1.place(x=380, y=100)
    display = Label(imageFrame1)
    display.imgtk = tkimage1
    display.configure(image=tkimage1)
    display.grid()

def edge_img():
    img_blur = resized.filter(ImageFilter.FIND_EDGES)
    tkimage1 = ImageTk.PhotoImage(img_blur)
    imageFrame1 = Frame(window)
    imageFrame1.place(x=380, y=100)
    display = Label(imageFrame1)
    display.imgtk = tkimage1
    display.configure(image=tkimage1)
    display.grid()

def original_img():
    tkimage1 = ImageTk.PhotoImage(resized)
    imageFrame1 = Frame(window)
    imageFrame1.place(x=380, y=100)
    display = Label(imageFrame1)
    display.imgtk = tkimage1
    display.configure(image=tkimage1)
    display.grid()

def exit_img():
    if not messagebox.askyesno("Exit Dialog", "Are you sure?"):
        messagebox.showinfo("", "Welcome Back")
    else:
        exit()

def close_form():
    if messagebox.askyesno("Exit Dialog", "Are you sure?"):
        exit()

window.protocol("WM_DELETE_WINDOW",close_form)

btn_open_img=Button(text = 'Open Image',fg = 'black',borderwidth = 0,command=open_img)
btn_open_img.place(x = 530, y = 10,width = 100,height = 70)

btn_save_img=Button(text = 'Save Image',fg = 'black',borderwidth = 0,command=save_img)
btn_save_img.place(x = 10, y = 10,width = 94,height = 70)

btn_save_as_img=Button(text = 'Save As Image',fg = 'black',borderwidth = 0,command=save_as)
btn_save_as_img.place(x = 10, y = 93,width = 94,height=70)

btn_resize_img=Button(text = 'Resize Image',fg = 'black',borderwidth = 0,command=resize_img)
btn_resize_img.place(x = 10, y = 176,width = 94,height=70)

btn_black_white_img=Button(text = 'Black And White',fg = 'black',borderwidth = 0,command=black_white)
btn_black_white_img.place(x = 10, y =260 ,width = 94,height=70)

btn_add_img=Button(text = 'Combine Image',fg = 'black',borderwidth = 0,command=combine_img)
btn_add_img.place(x = 10, y =342 ,width = 94,height=70)

btn_rotate_img=Button(text = 'Rotate Image',fg = 'black',borderwidth = 0,command=rotate_img)
btn_rotate_img.place(x = 10, y =425 ,width = 94,height=70)

btn_blur_img=Button(text = 'Blur ]mage',fg = 'black',borderwidth = 0,command=blur_img)
btn_blur_img.place(x = 120, y =10 ,width = 94,height=70)

btn_gaussian_img=Button(text = 'Contour ]mage',fg = 'black',borderwidth = 0,command=gaussian_img)
btn_gaussian_img.place(x = 120, y =93 ,width = 94,height=70)

btn_bilateral_filter_img=Button(text = 'Emboss ]mage',fg = 'black',borderwidth = 0,command=EMBOSS_img)
btn_bilateral_filter_img.place(x = 120, y =176 ,width = 94,height=70)

btn_edge_detection_img=Button(text = 'Edge ]mage',fg = 'black',borderwidth = 0,command=edge_img)
btn_edge_detection_img.place(x = 120, y =260 ,width = 94,height=70)

btn_original_img=Button(text = 'Original ]mage',fg = 'black',borderwidth = 0,command=original_img)
btn_original_img.place(x = 120, y =342 ,width = 94,height=70)

btn_exit_img=Button(text = 'EXIT',fg = 'black',borderwidth = 0,command=exit_img)
btn_exit_img.place(x = 120, y =425 ,width = 94,height=70)

window.mainloop()
