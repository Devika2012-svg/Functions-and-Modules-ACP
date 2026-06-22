import turtle

screen = turtle.Screen()
screen.bgcolor("#FFF8FC") 

t = turtle.Turtle()
t.speed(5)
t.pensize(8)

colors = ["#FFB6C1", "#D8BFD8", "#ADD8E6", "#ADE6B0", "#EDD8A0"]

for color in colors:
    t.pencolor(color)
    t.forward(150)
    t.right(90)

t.penup()
t.goto(45, -65)
t.pendown()
t.pencolor("#DDA0DD")

for _ in range(5):
    t.forward(60)
    t.right(144)

turtle.done()
