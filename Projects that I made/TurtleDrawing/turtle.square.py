from turtle import *

drawing_board = Screen()
drawing_board.bgcolor("indianred")
drawing_board.title("Alperen's Turtle")

turtle_instance = Turtle()
for i in range(0, 4):
    turtle_instance.forward(300)
    turtle_instance.left(90)
done()
