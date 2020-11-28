# imports
import turtle
# This following line may have been redundant
from turtle import Turtle

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
bullet1.color("orange")
bullet1.shape("square")

#Create Bomber
bomber = turtle.Turtle()
bomber.speed(0)
bomber.penup()
bomber.color("green")
bomber.shape("circle")
bomber.setpos(300, 300)


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


def bullet_reset():
    global bulletIsFired
    bulletIsFired = 0
    bullet1.hideturtle()
    bullet1.penup()
    bullet1.setpos(0, 0)


def touchbomber(bulletx,bullety):
    if bomber.distance(bulletx, bullety) < 15:
        bomber.speed(0)
        bomber.setpos(1000, 900)
        bullet_reset()

def timer():
    bullet_timer()
    wn.ontimer(timer, bulletDelay)


def bullet_timer():
    global bulletIsFired
#    print("bullet timer called")
    if bulletIsFired == 1:

        #print("bullet is fired")
        bullet1.forward(10)
        currentbulletpos = bullet1.pos()
        touchbomber(currentbulletpos[0],currentbulletpos[1])

        if (isoutofbounds(currentbulletpos)):
            bullet_reset()


def isoutofbounds(currentbulletpos):
    # print(currentbulletpos[0])
    # print(currentbulletpos[1])
    localx = currentbulletpos[0]
    y = currentbulletpos[1]

    # TODO: Try to use screensize method to do this test
    return localx > 500 or localx < -500 or y > 400 or y < -400


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

timer()

turtle.mainloop()
