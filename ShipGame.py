# imports
import turtle
# This following line may have been redundant
from turtle import Turtle
# Now let's start the project
from typing import Tuple

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1000, height=800)
x = 0
direction = 0

# Create Ship
ship = turtle.Turtle()
ship.setheading(0)
ship.color("red")
ship.shape("arrow")


# Create Bullet State

bulletIsFired = 0
bulletDelay = 50



# Create Bullet
bullet1 = turtle.Turtle()
bullet1.hideturtle()

bullet1.penup()
bullet1.color("blue")
bullet1.shape("square")

#Create Bomber
bomber=turtle.Turtle()
bomber.speed(0)
bomber.penup()
bomber.color("green")
bomber.shape("circle")
bomber.setpos(300,300)


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


def touchbomber(bulletx,bullety):
    global bulletIsFired
    if bomber.distance(bulletx,bullety)<15:
        bomber.speed(0)
        bomber.setpos(1000,900)
        bulletIsFired = 0
        bullet1.hideturtle()
        bullet1.penup()
        bullet1.setpos(0, 0)


def bullet_timer():
    global bulletIsFired
    global currentbulletpos
#    print("bullet timer called")
    if bulletIsFired==1:

        #print("bullet is fired")
        bullet1.forward(10)
        currentbulletpos = bullet1.pos()
        touchbomber(currentbulletpos[0],currentbulletpos[1])

        if (isoutofbounds(currentbulletpos)):
            bulletIsFired = 0
            bullet1.hideturtle()
            bullet1.penup()
            bullet1.setpos(0, 0)
    wn.ontimer(bullet_timer, bulletDelay)


def isoutofbounds(currentbulletpos):
    # print(currentbulletpos[0])
    # print(currentbulletpos[1])
    return(currentbulletpos[0] > 500 or currentbulletpos[0] < -500 or currentbulletpos[1] > 400 or currentbulletpos[1] < -400)


def shoot_bullet():
    global direction
    global bulletIsFired
    global ship

    if bulletIsFired == 0:
        bulletIsFired = 1
#        bullet1.setheading(direction)
        print(ship.heading())
        bullet1.setheading(ship.heading())
        bullet1.showturtle()

    direction = 270 + x


def turtleend():
    global wn

    wn.bye()


# Setup Turtle
turtle.listen()
turtle.onkey(turn_right, "Right")
turtle.onkey(turn_left, "Left")
turtle.onkey(shoot_bullet, "space")
turtle.onkey(turtleend, "Escape")

bullet_timer()

turtle.mainloop()
