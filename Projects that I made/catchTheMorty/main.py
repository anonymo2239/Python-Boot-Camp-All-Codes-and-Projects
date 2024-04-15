# rekor 273
from turtle import *
import time
from random import *

score = 0
pen2Value = Turtle()
pen2Value.hideturtle()


def yaz(message, pos):
    pen2Value.speed(0)
    x, y = pos
    pen2Value.penup()
    pen2Value.goto(x, y)
    pen2Value.color('darkgreen')
    style = ('Stencil Std', 30, 'normal')
    pen2Value.write(message, font=style)


def yaz2(message, pos):
    pen2Value.speed(0)
    x, y = pos
    pen2Value.penup()
    pen2Value.goto(x, y)
    pen2Value.color('black')
    style = ('Montserrat', 20, 'normal')
    pen2Value.write(message, font=style)


morty = Turtle()
pen3Value = Turtle()
pen3Value.hideturtle()


def main():
    global score
    score = 0
    pen2Value.clear()
    pen3Value.clear()
    morty.clear()
    yaz2("Score:", (-80, 270))
    yaz2("Time:", (-80, 230))
    window.addshape('icegif-1320 (2).gif')
    morty.shape('icegif-1320 (2).gif')
    morty.penup()
    morty.speed(0)
    countdown(40)
    done()


def yaz3(message, pos):
    pen3Value.speed(0)
    x, y = pos
    pen3Value.penup()
    pen3Value.goto(x, y)
    pen3Value.color('black')
    style = ('Montserrat', 20, 'normal')
    pen3Value.write(message, font=style)


def mortyClick(x, y):
    pen3Value.clear()
    time.sleep(0.0000000000000000000001)
    global score
    score += 1
    yaz3(str(score), (10, 270))


def mortyClick2(x, y):
    global score
    score += 1


def space_restart():
    main()


def esc_finish():
    quit()


def countdown(t):
    pen2Value = Turtle()
    pen2Value.clear()
    pen2Value.hideturtle()
    pen2Value.penup()
    pen2Value.speed(0)
    pen2Value.left(180)
    pen2Value.forward(0)
    pen2Value.right(90)
    pen2Value.forward(229)
    pen2Value.right(90)

    while t >= 0:
        freq = 0.5
        morty.hideturtle()
        pen2Value.clear()
        if score == 0:
            yaz3(str(score), (10, 270))
        # timer1
        mins, secs = divmod(t, 60)
        timer = '{:}'.format(secs)
        pen2Value.write(str(int(int(timer) * freq)), True, "left", ("Montserrat", 20, "normal"))
        if int(int(timer) * freq) <= 9:
            pen2Value.backward(15)
        elif int(int(timer) * freq) <= 14 and int(int(timer) * freq) > 9:
            pen2Value.backward(24)
        else:
            pen2Value.backward(25.6)

        # spawning
        numx = randint(-400, 400)
        numy = randint(-330, 330)
        morty.setx(numx)
        morty.sety(numy)
        morty.showturtle()

        time.sleep(freq)
        t -= 1

        if t == 0:
            yaz(f"    Your score: {score}\n      Game Over\nPress space to start\n   Press Esc to quit", (-210, 0))
            morty.onclick(mortyClick2)
            window.onkey(space_restart, "space")
            window.onkey(esc_finish, "Escape")
            listen()
        else:
            morty.onclick(mortyClick)
    pen2Value.clear()

window = Screen()
window.bgpic("682996-991246141.png")
window.title("Catch the Morty")

if __name__ == '__main__':
    main()

window.mainloop()