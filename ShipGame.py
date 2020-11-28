# imports
import turtle
# This following line may be redundant
from turtle import Turtle

wn = turtle.Screen()
wn.bgcolor("black")
x = 0
direction = 0

# Create Ship
ship = turtle.Turtle()
ship.setheading(0)
ship.color("red")
ship.shape("arrow")


# Create Bullet State
bulletIsFired = 0
bulletDelay = 100



# Create Bullet
bullet1 = turtle.Turtle()
bullet1.hideturtle()

bullet1.penup()
bullet1.color("blue")
bullet1.shape("square")
"""bomber=turtle.Turtle()
bomber.color("green")
bomber.shape("circle")"""


def turn_right():
    global direction
    ship.right(5)
    direction = direction - 5
    if direction < 0:
        x = 0 - direction

        direction = 270 + x


def turn_left():
    global direction
    ship.left(5)
    direction = direction + 5
    if direction < 0:
        x = 0 - direction


def bullet_timer():
    print "bullet timer called"
    if (bulletIsFired):
        print "bullet is fired"
        bullet1.forward(10)
        currentbulletpos = bullet1.pos()
        print currentbulletpos[0]
        print currentbulletpos[1]
    wn.ontimer(bullet_timer, bulletDelay)

def shoot_bullet():
    global direction
    global bulletIsFired

    if bulletIsFired == 0:
        bulletIsFired = 1
        bullet1.setheading(direction)
        bullet1.showturtle()


    direction = 270 + x


# Setup Turtle
turtle.listen()
turtle.onkey(turn_right, "Right")
turtle.onkey(turn_left, "Left")
turtle.onkey(shoot_bullet, "space")

bullet_timer()

turtle.mainloop()
