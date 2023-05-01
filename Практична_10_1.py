from tkinter import *


def button_click():
	entry["bg"] = "red"
	entry["fg"] = "white"
	entry["font"] = ("Arial", 14)
	entry["width"] = entry["width"] + 6 
	entry.delete(0, END)
	entry.insert(0, "Ми використовуємо властивості поля!")


root = Tk()

entry = Entry(width = 15, bd = 5)
entry.pack(padx = 30)
entry.insert(0, "8 клас")


button = Button(text = "Виконати", command = button_click)
button.pack()


root.mainloop()