from turtle import Turtle, Screen
import turtle

tim = Turtle()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_clockwise():
    tim.right(10)


def move_a_clockwise():
    tim.left(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen = Screen()
turtle.listen()
turtle.onkey(key="w", fun=move_forward)
turtle.onkey(key="s", fun=move_backward)
turtle.onkey(key="d", fun=move_clockwise)
turtle.onkey(key="a", fun=move_a_clockwise)
turtle.onkey(key="c", fun=clear_screen)
screen.exitonclick()
