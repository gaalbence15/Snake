import turtle
import time


def jobbra():
    fej.right(90)


def balra():
    fej.left(90)


palya = turtle.Screen()
palya.setup(width=800, height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)
palya.listen()
palya.onkey(jobbra, "Right")
palya.onkey(balra, "Left")

fej = turtle.Turtle()
fej.shape("triangle")
fej.penup()
fej.color("yellow")

gameover = turtle.Turtle()
gameover.color("yellow")
gameover.hideturtle()
gameover.penup()

while True:
    fej.forward(20)
    palya.update()
    time.sleep(0.2)

    if fej.ycor() > 300 or fej.ycor() < -300:
        gameover.write("Game Over!", font=("Arial", 20, "bold"), align="center")
        fej.clear()

    if fej.xcor() > 400 or fej.xcor() < -400:
        gameover.write("Game Over!", font=("Arial", 20, "bold"), align="center")
        fej.clear()
