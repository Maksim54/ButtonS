from tkinter import *
import tkinter as tk
import sys
from tkinter import ttk
import tkinter
from tkinter import messagebox
def buttonCallback():
    messagebox.showinfo("Message", "You have clicked the Button!")
def Exit():
    root.quit()
root = Tk()
root.title('Functions')
root.iconbitmap('function.ico')
root.configure(bg='orange')
root.geometry('400x200')
btn1 = tkinter.Button(height=2,width=8,text = "Resolution", bg = "darkmagenta",fg='thistle',command=lambda:root.geometry('800x600'))#'fg or foreground is for coloring the contents (buttons)
btn2 = tkinter.Button(height=2,width=8,text = "Background", bg = "darkmagenta",fg='thistle',command=lambda:root.config(bg='grey'))
btn3 = tk.Button(height=2,width=8,fg='thistle',bg='darkmagenta',text="Click", command=buttonCallback)
button_three = tk.Button(root,height=2,width=8,bg='darkmagenta',fg='thistle',text = "Exit",command = Exit)#кнопка для выхода из программы
button_three.pack()
#
top = Tk()
top.title('Random buttons')
top.iconbitmap('button.ico')
top.configure(bg='lime')
top.geometry("300x150")
def click():
    messagebox.showinfo('Wow!', 'You clicked the Green button')
def clik():
    messagebox.showinfo('Wow!','You clicked the Blue button')
def clikk():
    messagebox.showinfo('Wow!','You clicked the Red button')
def clickk():
    messagebox.showinfo('Wow!','You clicked the Yellow button')
a = Button(top, text="Yellow", fg="black",command=clickk,activebackground='yellow',bg="orange")
b = Button(top, text="Blue", fg="black",command=clik,activebackground='blue', bg="orange")
c = Button(top, text="Green", command=click, fg = "black",bg='orange', activebackground="green")
d = Button(top, text="Red", fg="black",command=clikk,bg='orange', activebackground="red")
#
a.pack(side = LEFT)
b.pack(side = RIGHT)
c.pack(side = TOP)
d.pack(side = BOTTOM)
#
root = Toplevel()
root.title('Lunar')
root.iconbitmap('iconn.ico')
img = tk.PhotoImage(file="lunar.png")
#
label = tk.Label(root, image=img)
label.pack()
#
root.configure(bg='aliceblue')#концигурации главного окна
btn1.pack()
btn2.pack()
btn3.pack()
root.mainloop()


