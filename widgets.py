from tkinter import *
from datetime import date

root = Tk()
root.title("Widgets Example")
root.geometry("400x300")

lbl = Label(text="Hey there", fg="blue", font=("Arial", 16), bg="yellow", width=300, height=1)

name_lbl = Label(text="Name:", bg="lightgray")
name_entry = Entry()

def display():
    name= name_entry.get()
    global message
    message = "Welcome! \n Today's date is:"
    greet= "Hello " + name+ "\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text( height=3)

btn = Button(text="Begin", command=display, height=1, bg="green", fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()