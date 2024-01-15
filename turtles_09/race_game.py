import time
import random
from turtle import Turtle, Screen

game_end = False
# Listener function
def move_func():
    if not game_end:
        green_turtle.forward(5)




my_turtle = Turtle()

# Screen setup
my_screen = Screen()
my_screen.title("Race Game")
my_screen.setup(800, 500)
my_screen.bgcolor("forestgreen")

# Heading
my_turtle.penup()
my_turtle.goto(-100, 205)
my_turtle.color('White')
my_turtle.write('Turtle race', font=('Arial', 20,'bold'))


# The Floor

my_turtle.goto(-350, 200)
my_turtle.pendown()
my_turtle.color('chocolate')
my_turtle.begin_fill()
my_turtle.speed('slow')
for i in range(2):
    my_turtle.forward(700)
    my_turtle.right(90)
    my_turtle.forward(400)
    my_turtle.right(90)
my_turtle.end_fill()


# create function
def draw_turtle(t_name, t_color, t_y):
    t_name = Turtle()
    t_name.color(t_color)
    t_name.shape('turtle')
    t_name.shapesize(1.5)
    t_name.penup()
    t_name.goto(-300, t_y)
    t_name.pendown()
    t_name.speed('slowest')
    return t_name

# call function ( 4 times )
blue_turtle = draw_turtle(t_name='blue_turtle', t_color='cyan', t_y=150)
pink_turtle = draw_turtle(t_name='pink_turtle', t_color='pink', t_y=50)
yellow_turtle = draw_turtle(t_name='yellow_turtle', t_color='yellow', t_y=-50)
green_turtle = draw_turtle(t_name='green_turtle', t_color='green', t_y=-150)



# pause for 1 second before start the race :
time.sleep(1)

# Move the turtles
my_screen.listen()
my_screen.onkey(move_func, "Right")

while True:
    blue_turtle.forward(random.randint(1, 10))
    pink_turtle.forward(random.randint(1, 10))
    yellow_turtle.forward(random.randint(1, 10))
    # green_turtle.forward(random.randint(1, 10))

    if blue_turtle.xcor() > 230:
        winner = blue_turtle
        break
    elif pink_turtle.xcor() > 230:
        winner = pink_turtle
        break
    elif yellow_turtle.xcor() > 230:
        winner = yellow_turtle
        break
    elif green_turtle.xcor() > 230:
        winner = green_turtle
        break


# Celebrate the winner
game_end = True
winner.shapesize(2.5)
for i in range(1000):
    winner.right(5)



my_screen.exitonclick()