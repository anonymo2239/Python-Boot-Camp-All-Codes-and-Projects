import turtle

drawing_board = turtle.Screen() #Ekran Oluşturur
drawing_board.bgcolor("indianred") #arkaplan rengi
drawing_board.title("Alperen's Turtle")

turtle_instance = turtle.Turtle() # turtle kütüphanesinden tospa oluşturuyor.
turtle_instance.color("pink")
turtle_instance.forward(100)

turtle_instance_2 = turtle.Turtle() # 2. tospa
turtle_instance_2.right(721)
turtle_instance_2.forward(150)
turtle.done()

