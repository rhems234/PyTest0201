import turtle
import random

screen = turtle.Screen()


def screenLeftClick(x, y):
    t = turtle.Turtle()
    n = 50
    t.screen.bgcolor("black")
    t.color("yellow")
    t.speed(20)
    t.goto(x, y)
    for i in range(70):
        t.circle(80)
        t.left(360 / n)
        t.hideturtle()


def screenRightClick(x, y):
    t = turtle.Turtle()
    t.penup()
    t.goto(x, y)


def screenMidClick(x, y):
    t = turtle.Turtle()
    global r, g, b
    tSize = random.randrange(1, 10)
    t.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    t.pencolor((r, g, b))


pSize = 10
r, g, b = 0.0, 0.0, 0.0

turtle.title("거북이로 그림 그리기")
turtle.shape("turtle")
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
