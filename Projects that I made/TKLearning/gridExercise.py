import tkinter

def click_():
    alperen = int(my_entry2.get())
    my_label2.config(text=str(alperen * konsol))

pencere = tkinter.Tk()
pencere.minsize(width=550, height=450)
pencere.title("Gridview")


my_label2 = tkinter.Label()
my_label2.config(text="hi", font=("Montserrat", 15, "bold"))
my_label2.grid(row=0, column=0)
konsol = int(input("Konsola da bir sayı gir."))
my_button2 = tkinter.Button(text="Click on this multiple", command=click_)
my_button2.grid(row=1, column=1)

my_entry2 = tkinter.Entry()
my_entry2.config(width=15)
my_entry2.grid(row=2, column=2)

pencere.mainloop()