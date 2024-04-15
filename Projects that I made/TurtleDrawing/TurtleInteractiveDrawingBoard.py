import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light green")
drawing_board.title("Python Turtle")

tosba1 = turtle.Turtle()


def turtle_forward():
    tosba1.forward(30)


def clearScreen():
    tosba1.clear()


def backHome():
    tosba1.penup()
    tosba1.home()
    tosba1.pendown()


def penUp():
    tosba1.penup()


def penDown():
    tosba1.pendown()


drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="Up")
drawing_board.onkey(lambda: tosba1.setheading(tosba1.heading() - 30), "Right")
drawing_board.onkey(lambda: tosba1.left(30), "Left")  # 13. ile 14. satır aynı
drawing_board.onkey(clearScreen, "c")
drawing_board.onkey(backHome, "space")
drawing_board.onkey(penUp, "w")
drawing_board.onkey(penDown, "q")

turtle.done()
