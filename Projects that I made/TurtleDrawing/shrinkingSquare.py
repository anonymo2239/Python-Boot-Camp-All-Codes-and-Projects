import turtle

back = turtle.Screen()
back = turtle.bgcolor("Lightgray")
back = turtle.title("emegara")

batu = turtle.Turtle()

t = 1
for i in range(100):
    for j in range(4):
        batu.forward(300 / t)
        batu.left(90)
    t = t + 1
turtle.done()