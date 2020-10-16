# Project 2

from tkinter import *

window=Tk()
window.geometry("300x300")
window.title("TempConvert Web Service Client")
frame= Frame(window)
frame.pack()

inputnumber= StringVar()
var= StringVar()

mylabel= Label(window, text="Temperature Convert Web Service")
mylabel.pack(side = LEFT)
mylabel.place(x= 100, y= 25)

L1= Label(window, text= "F: ")
L1.pack(side= LEFT)
L1.place(x= 10, y= 50)
E1=Entry(window, textvariable = inputnumber)
E1.pack(side=LEFT)
E1.place(x= 25, y= 50)

L2= Label(window, text= "C: ")
L2.pack(side= LEFT)
L2.place(x= 250, y= 50)
E2= Entry(window, textvariable= inputnumber)
E2.pack(side= LEFT)
E2.place(x= 280,y= 50)

check_btn= Checkbutton(window, text="Fahrenheit to Celsius")
check_btn.pack(side=LEFT)
check_btn.place(x= 35,y= 100)

check_btn= Checkbutton(window, text="Celsius to Fahrenheit" )
check_btn.pack(side=LEFT)
check_btn.place(x= 270,y= 100)

def convert():
    
cbutton=Button(window,text= "Convert", command= convert)
cbutton.pack(side= BOTTOM)
cbutton.place(x= 30, y= 150)

qbutton=Button(window, text="Quit")
qbutton.pack(side= BOTTOM)
qbutton.place(x= 280,y= 150)

window.mainloop()




