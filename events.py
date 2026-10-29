from tkinter import *

window= Tk()
window.title("Events")
window.geometry("100x100")

def handle_press(event):
    """Print the character associated with the key pressed."""
    print(event.char)

window.bind("<Key>", handle_press)

def handle_click(event):
    print("\n the button was clicked")

button= Button(text="Click Me")
button.pack()
button.bind("<Button-1>", handle_click)

window.mainloop()