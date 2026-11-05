from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root=Tk()
root.title("Denominator Calculator")
root.geometry("650x400")
root.configure(bg="lightblue")


upload= Image.open("denominator.webp")
upload= upload.resize((300, 300))
image= ImageTk.PhotoImage(upload)

label= Label(root, image=image, bg="lightblue")
label.place(x=180, y=20)

label1= Label(root, text= "Hey there! Welcome to the Denominator Calculator", bg="lightblue")
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    Msg= messagebox.showinfo("Alert", "do you want to continue with the calculator?")
    if Msg== "ok":
        topwin()

button1= Button(root, text= "Lets go!", command= msg, bg="lightgreen", fg="grey", font=("Arial", 12, "bold"))
button1.place(x= 260,y=370)

def topwin():
    top= Toplevel()
    top.title("Denominator Calculator")
    top.configure(bg="lightblue")
    top.geometry("600x350+50+50")

    label= Label(top, text="Enter the total amount:", bg="lightblue")
    entry= Entry(top)

    lbl= Label(top, text="Here are the number of notes for each denomination:", bg="lightblue")

    l1= Label(top, text="100:", bg="lightblue")
    l2= Label(top, text="50:", bg="lightblue")
    l3= Label(top, text="10:", bg="lightblue")

    t1= Entry(top)
    t2= Entry(top)
    t3= Entry(top)

    def calculator():
        try:
            amount= int(entry.get())

            note100= amount//100
            amount%=100

            note50= amount//50
            amount%=50

            note10= amount//10

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note100))
            t2.insert(END, str(note50))
            t3.insert(END, str(note10))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer amount.")

    btn= Button(
        top,
        text="Calculate",
        command=calculator,
        bg="lightgreen",
        fg="grey",

    )

    label.place(x=230, y=50)            
    entry.place(x=200, y=80)
    btn.place(x=250, y=110)

    lbl.place(x=140, y=170)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()