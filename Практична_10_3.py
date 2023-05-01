from tkinter import *


def button_click():
	cookies = float(entryl.get())
	milk = float(entry2.get())
	bread = float(entry3.get())
	money = float(entry4.get())
	result = money-(cookies*4+2*milk+bread)
	label5['text'] = "У Марійки залишилося - " + str(result)


root = Tk()
root.geometry("300x250")


labell = Label(text = "Ціна печива (100 г)")
labell.pack()
entryl = Entry()
entryl.pack ()
label2 = Label(text = "Ціна пакета молока")
label2.pack()
entry2 = Entry()
entry2.pack ()
label3 = Label(text = "Ціна хліба")
label3.pack()
entry3 = Entry()
entry3.pack()
label4 = Label(text = 'Кошти (грн.)) ')
label4.pack()
entry4 = Entry()
entry4.pack()
button = Button(text = 'Обчислити', command = button_click)
button.pack()
label5 = Label()
label5.pack(pady = 5)


mainloop()