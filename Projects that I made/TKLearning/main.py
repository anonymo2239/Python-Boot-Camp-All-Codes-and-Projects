import tkinter

#We must write functions above buttons,labels ets.
def click_button():
    userAnswer = myEntry.get()
    print(userAnswer)

#window
window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=550, height=300)
window.update()
print(window.winfo_width())

#label
my_label = tkinter.Label(text="Hoşgeldiniz")
#my_label.config(bg="black", fg="white") #config = yapılandırma
my_label.config(font=("Arial", 35, "bold italic"))
#my_label.pack(side="left")#pack elemanları genel olarak 4 farklı şekilde konumlandırmaya yarıyor
my_label.place(x=0, y=0)

#button
myButton = tkinter.Button(text="Click", command=click_button)
#myButton.pack(side="right")
myButton.update()
myButton.place(x=100, y=150)

#entry
myEntry = tkinter.Entry(width=15)
#myEntry.pack(side="right")
myEntry.place(x=240, y=200)

window.mainloop()