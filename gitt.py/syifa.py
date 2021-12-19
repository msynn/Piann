import turtle

turtle.bgcolor("black")
turtle.pensize(4)
turtle.title("Nursyifa Iqxan")

def curve():
    for i in range (215):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(0.1)
turtle.color("white","yellow")

turtle.begin_fill()
turtle.left(145)
turtle.forward(110.80)
curve()

turtle.left(145)
curve()
turtle.forward(110.80)
turtle.end_fill()
turtle.hideturtle