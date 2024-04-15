import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("lightgreen")

turtle1 = turtle.Turtle()
turtle1.color("Dark green")

turtleColor = ["blue", "yellow", "green", "pink", "white", "red", "orange"]

for i in range(1 ,10):
    turtle1.color(turtleColor[i % 7])
    turtle1.circle(10 * i)
    turtle1.circle(- 10 * i)

turtle.done()
