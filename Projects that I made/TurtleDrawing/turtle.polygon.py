import turtle

arka = turtle.Screen()
arka.bgcolor("Lightblue")
arka.title("tosbaa")

tosba = turtle.Turtle()
option = str(input("Yıldız mı Poligon mu çizdireceksiniz?\n"))
if(option.lower() == "yıldız" or option.lower() == "yildiz"):
    tosba.right(36)
    for i in range(5):
        tosba.left(144)
        tosba.forward(300)
    turtle.done()
elif(option.lower() == "poligon"):
    sideNum = int(input("Kaç kenarlı olacak?\n"))
    for j in range(sideNum):
        tosba.left(360/sideNum)
        tosba.forward(150)
    turtle.done()

