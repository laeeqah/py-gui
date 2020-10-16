from tkinter import *


window = Tk()
window.geometry("300x300")
window.title("Adding two number")
frame = Frame(window)
frame.pack()

num_1= IntVar()
num_2= IntVar()
num_3= IntVar()

L1 = Label(window, text="Please enter first number: ")
L1.pack( side= LEFT)
L1.place(x= 1, y= 10)

E1 = Entry(window, bd = 5)
E1.pack(side = RIGHT)
E1.place(x= 200, y= 5)

frame2 =Frame (window)
frame2.pack()
L2 = Label(window, text="Please enter second number: ")
L2.pack(side = RIGHT)
L2.place(x = 1, y = 50)

E2 =Entry (window, bd = 5)
E2.pack(side = RIGHT)
E2.place(x= 200, y= 50)

frame3= Frame(window)
frame3.pack()
L3 = Label(window, text="Your answer: ")
L3.pack(side = RIGHT)
L3.place(x= 1, y= 100)

E3 =Entry (window,bd = 5)
E3.pack(side = RIGHT)
E3.place(x= 200, y= 100)



def add_num():

    E3.insert(END, int(num_1.get()) + int(num_2.get()))

add_btn = Button(text="Add", command=add_num, width=10 ,height= 2)
add_btn.pack(side=LEFT)

def clear_all_num():
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)

clear_btn= Button(text="clear", command=clear_all_num, width=10, height= 2)
clear_btn.pack(side= LEFT)

def exit_all():
    window.destroy()

exit_btn= Button(text= "Exit", command =exit_all, width=10, height= 2)
exit_btn.pack(side= LEFT)

window.mainloop()













