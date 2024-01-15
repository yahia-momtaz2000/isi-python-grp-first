# from module turtle import classes Turtle, Screen
from turtle import Turtle, Screen

# create new object from Turtle class
my_turtle1 = Turtle()
my_turtle1.shape('turtle')
my_turtle1.speed('slowest')
my_turtle1.fillcolor('green')
my_turtle1.begin_fill()
for i in range(1, 3):
    my_turtle1.forward(100)
    my_turtle1.left(90)
    my_turtle1.forward(150)
    my_turtle1.left(90)
my_turtle1.end_fill()

my_turtle1.penup()
my_turtle1.forward(200)
my_turtle1.pendown()
my_turtle1.left(90)
my_turtle1.forward(150)

# screen option
my_screen = Screen()
my_screen.exitonclick()