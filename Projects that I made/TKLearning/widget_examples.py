from tkinter import *

window = Tk()
window.title = "Python Tkinter"
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

my_label = Label(text="My label")
my_label.config(font=("Montserrat", 22, "normal"))
my_label.config(padx=20, pady=20)
my_label.pack()

def button_clicked():
    print("button clicked")
    print(myEntry1453.get())
    print(myText1466.get("3.0", END))
    #3.0 --- 3 -> line, 0 -> character

buttonAlp = Button(text="Click", command=button_clicked)
buttonAlp.pack()
buttonAlp.config(padx=20, pady=20)
buttonAlp.focus()

myEntry1453 = Entry(width=15)
myEntry1453.pack()

myText1466 = Text(width=20, height=5)
myText1466.pack()

#scale
def scale_selected(value):
    print(value)
    print(mySpinbox.get())
myScale = Scale(from_=0, to=50)
myScale.config(command=scale_selected)
myScale.pack(side="right")

#spinbox
mySpinbox = Spinbox(from_=0, to=50)
mySpinbox.pack()

#checkbutton
def checkButton_selected():
    print(myCheckVariable.get())
myCheckVariable = BooleanVar()
myCheck = Checkbutton(text="Futbol", variable=myCheckVariable, command=checkButton_selected)
myCheck.pack()

#radioButton
def radioButtonSelected():
    print(myRadioButtonVar.get())
myRadioButtonVar = IntVar()
myRadioButton = Radiobutton(text="Red Pill", value=10, variable=myRadioButtonVar, command=radioButtonSelected)
myRadioButton2 = Radiobutton(text="Blue Pill", value=0, variable=myRadioButtonVar, command=radioButtonSelected)
myRadioButton.pack()
myRadioButton2.pack()

#listbox
def listboxSelected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
name_list = ["Alperen", "Arda", "Adem", "Alper"]
for i in range(len(name_list)):
    my_listbox.insert(i, name_list[i])
my_listbox.pack()
my_listbox.bind('<<ListboxSelect>>', listboxSelected) #listbox'a özgü bir şey dokümandan okunmalı.

window.mainloop()