import tkinter as tk

window = tk.Tk()
window.eval('tk::PlaceWindow . center')
window.title("BMI Calculator")
window.config(bg="lightgray")
window.minsize(width=280, height=250)

def calculate_bmi():
    lblResult = tk.Label()
    try:
        cm = float(entryHeight.get())
        kg = float(entryWeight.get())
        bmi = round(kg/((cm/100) ** 2), 3)
        if 10 <= bmi < 20:
            lblResult.config(text=f"You are within the Underweight range\n with your {bmi} Body Mass value.", bg="lightgray")
            lblResult.place(x=0, y=0)
            window.update()
            lblResult.place(x=window.winfo_width()/2 - lblResult.winfo_width()/2, y=185)
        elif 20 <= bmi < 25:
            lblResult.config(text=f"You are within the Healthy range\n with your {bmi} Body Mass value.", bg="lightgray")
            lblResult.place(x=0, y=0)
            window.update()
            lblResult.place(x=window.winfo_width() / 2 - lblResult.winfo_width() / 2, y=185)
        elif 25 <= bmi < 30:
            lblResult.config(text=f"You are within the Overweight range\n with your {bmi} Body Mass value.", bg="lightgray")
            lblResult.place(x=0, y=0)
            window.update()
            lblResult.place(x=window.winfo_width() / 2 - lblResult.winfo_width() / 2, y=185)
        elif 30 <= bmi < 40:
            lblResult.config(text=f"You are within the Overweight range\n with your {bmi} Body Mass value.", bg="lightgray")
            lblResult.place(x=0, y=0)
            window.update()
            lblResult.place(x=window.winfo_width() / 2 - lblResult.winfo_width() / 2, y=185)
        elif 40 <= bmi < 90:
            lblResult.config(text=f"You are within the Overweight range\n with your {bmi} Body Mass value.", bg="lightgray")
            lblResult.place(x=0, y=0)
            window.update()
            lblResult.place(x=window.winfo_width() / 2 - lblResult.winfo_width() / 2, y=185)
        else:
            lblResult.config(text="This value does not exist in any range.         \n                 ", bg="lightgray")
            lblResult.place(x=0, y=0)
            window.update()
            lblResult.place(x=window.winfo_width() / 2 - lblResult.winfo_width() / 2, y=185)
    except:
        lblResult.config(text="       Please enter a valid number.       ", bg="lightgray")
        lblResult.place(x=0, y=0)
        window.update()
        lblResult.place(x=window.winfo_width() / 2 - lblResult.winfo_width() / 2, y=185)
        if entryHeight.get() == "" or entryWeight.get() == "":
            lblResult.config(text="Please enter both weight and height.", bg="lightgray")
            lblResult.place(x=0, y=0)
            window.update()
            lblResult.place(x=window.winfo_width() / 2 - lblResult.winfo_width() / 2, y=185)

lblWeight = tk.Label(window, text="Enter Your Weight(kg)", bg="lightgray")
lblWeight.config(font=("Montserrat", 11))
lblWeight.place(x=0, y=30)
window.update()
lblWeight.place(x=window.winfo_width()/2 - lblWeight.winfo_width()/2, y=30)

entryWeight = tk.Entry()
entryWeight.place(x=0, y=60)
window.update()
entryWeight.place(x=window.winfo_width()/2 - entryWeight.winfo_width()/2, y=60)

lblHeight = tk.Label(window, text="Enter Your Height(cm)", bg="lightgray")
lblHeight.config(font=("Montserrat", 11))
lblHeight.place(x=88, y=90)
window.update()
lblHeight.place(x=window.winfo_width()/2 - lblWeight.winfo_width()/2, y=90)

entryHeight = tk.Entry()
entryHeight.place(x=0, y=60)
window.update()
entryHeight.place(x=window.winfo_width()/2 - entryWeight.winfo_width()/2, y=120)

btnCalculate = tk.Button(text="Calculate", command=calculate_bmi)
btnCalculate.place(x=0, y=0)
window.update()
btnCalculate.place(x=window.winfo_width()/2 - btnCalculate.winfo_width()/2, y=150)

window.mainloop()