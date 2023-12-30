#Import tkinter library
from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
def callback(event):
   win.destroy()
#Create a Label and a Button widget
label=ttk.Label(win, text="Press Enter to Close the Window", font=('Century 17 bold'))
label.pack(ipadx=10)
win.bind('<Return>',callback)
#Disable the Mouse Pointer
win.config(cursor="none")
win.mainloop()