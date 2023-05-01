from tkinter import *


def button_click():
	a = float(entry1.get())
	b = float(entry2.get())
	result = a*(4*b-a)
	label3["text"] = "Рузальтат = " + str(result)

root = Tk()

labell = Label(text = "a =")
labell.pack()
entry1 = Entry()
entry1.pack()
label2 = Label(text = "b =")
label2.pack()
entry2 = Entry()
entry2.pack()
label3 = Label()
label3.pack()
button = Button(text = "Обчислити", command = button_click)
button.pack()


mainloop()