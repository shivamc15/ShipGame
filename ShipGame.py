# imports
import turtle
# This following line may have been redundant
from turtle import Turtle
import ShipGameBomber

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1000, height=800)
delay=10
#Creating Line where Bomber spawns
linebuilder = turtle.Turtle()
linebuilder.speed(0)
linebuilder.hideturtle()
linebuilder.pencolor("white")
linebuilder.penup()
linebuilder.setpos(-300, -300)
linebuilder.pendown()
linebuilder.setpos(-300, 300)
linebuilder.setpos(300, 300)
linebuilder.setpos(300, -300)
linebuilder.setpos(-300, -300)
x = 0
direction = 0

# Create Ship
ship = turtle.Turtle()
ship.setheading(0)
ship.color("red")
ship.shape("arrow")

# Create Bullet State

bulletIsFired = 0
bulletDelay = 3

# Create Bullet
bullet1 = turtle.Turtle()
bullet1.hideturtle()

bullet1.penup()
bullet1.color("orange")
bullet1.shape("square")

# Create Bomber
bomber1 = ShipGameBomber.Bomber(300, 300)
bomber1.makeactive()
bomberlist = [bomber1]

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


def touchbomber(bomber, bullet):
    if bomber.istouchingBullet(bullet):
        bomber.makeinactive()
        bullet_reset()
        wn.ontimer(bomber.makeactive, 1000)

def timer():
    bullet_timer()
    bomber_timer()
    wn.ontimer(timer, bulletDelay)


def bomber_timer():
    global bomberlist
    for bomber in bomberlist:
        bomber.moveforward()
        if bomber.ishittingship():
            turtleend()


def bullet_timer():
    global bulletIsFired
    global bomberlist

    if bulletIsFired == 1:
        bullet1.forward(10)
        for bomber in bomberlist:
            touchbomber(bomber, bullet1)

        if (isoutofbounds(bullet1.pos())):
            bullet_reset()


def isoutofbounds(currentbulletpos):
    localx = currentbulletpos[0]
    y = currentbulletpos[1]

    # TODO: Try to use screensize method to do this test
    return localx > 300 or localx < -300 or y > 300 or y < -300


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
    print("Turtle end called")
    wn.bye()


# Setup Turtle
turtle.listen()
turtle.onkey(turn_right, "Right")
turtle.onkey(turn_left, "Left")
turtle.onkey(shoot_bullet, "space")
turtle.onkey(turtleend, "Escape")

timer()

turtle.mainloop()

