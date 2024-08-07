from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

label = Label(text="Label", font=("Arial", 24, "bold"))
label.grid(column=1, row=1)  # Corrected here
label["text"] = "ceva"

input = Entry(width=10)
input.grid(column=2, row=1)  # Corrected here

def do_smt():
    print("sum")
    ceva_input = input.get()
    label.config(text=ceva_input)

button = Button(text="click me", command=do_smt)
button.grid(column=1, row=2)  # Corrected here

window.mainloop()
