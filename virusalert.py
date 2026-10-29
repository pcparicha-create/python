from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Virus Alert")
root.geometry("400x400")

def msg():
    messagebox.showwarning("virus detected")

button= Button(root,text="Virus Alert", command=msg )
button.place(x=60, y=100)

root.mainloop()
