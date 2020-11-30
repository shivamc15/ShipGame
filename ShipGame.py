# imports
import turtle
import time
import random
#Creating a class for a bomber so we can create multiple similiar bombers
class Bomber:

    isVisible = 0
    startingposx = 0
    startingposy = 0
    bturtle = 0

    def __init__(self, posx, posy):
        self.startingposx = posx
        self.startingposy = posy
        self.bturtle = turtle.Turtle()
        self.bturtle.speed(0)
        self.bturtle.penup()
        self.bturtle.color("green")
        self.bturtle.shape("circle")
        self.bturtle.hideturtle()
        # TODO: add code for turtle here

    def makeactive(self):
        self.isVisible = 1
        self.bturtle.setpos(self.startingposx, self.startingposy)
        angletoship = self.bturtle.towards(0, 0)
        self.bturtle.setheading(angletoship)
        self.bturtle.speed(2)
        self.bturtle.showturtle()

    def makeinactive(self):
        self.isVisible = 0
        self.bturtle.speed(0)
        self.bturtle.setpos(self.startingposx, self.startingposy)
        self.bturtle.hideturtle()

    def moveforward(self):
        if self.isVisible == 1:
            self.bturtle.forward(3)

    def istouchingBullet(self, bullet):
        bulletpos = bullet.pos()
        return self.bturtle.distance(bulletpos[0], bulletpos[1]) < 15

    def ishittingship(self):
        return self.bturtle.distance(0, 0) < 15

starttime=round(time.time())

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1000, height=800)
turtle.color("white")


delay=10
gameoverstate=0

turtle.hideturtle()
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
bulletDelay = 1

# Create Bullet
bullet1 = turtle.Turtle()
bullet1.hideturtle()

bullet1.penup()
bullet1.color("orange")
bullet1.shape("square")

# Create Bomber
bomber1 = Bomber(300, 300)
bomber1.makeactive()
bomber2 = Bomber(0, 300)
bomber2.makeactive()
bomber3 = Bomber(-300, 300)
bomber3.makeactive()
bomber4 = Bomber(-300, -300)
bomber4.makeactive()
bomber5 = Bomber(300, 0)
bomber5.makeactive()
bomberlist = [bomber1,bomber2,bomber3,bomber4,bomber5]

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
    global gameoverstate
    global starttime
    bullet_timer()
    bomber_timer()
    """currenttime=time.time()
    if int(currenttime)-int(starttime)==100:
        starttime=starttime+100"""
    print("timer called")
    #timetimer()
    print("gameover value " + str(gameoverstate))
    if gameoverstate==0:
        print("setting up ontimer")
        wn.ontimer(timer, bulletDelay)
"""def timetimer():
    global timecontral
    timecontral = 0
    timecontral += 1
    turtle.hideturtle()
    turtle.penup()
    turtle.color("white")

    style = ('Courier', 30, 'italic')
    turtle.setpos(0, 350)
    turtle.write(str(starttime), font=style, align='center')
    turtle.hideturtle()"""
def bomber_timer():
    global bomberlist
    for bomber in bomberlist:
        bomber.moveforward()
        if bomber.ishittingship():
            gameover()


def bullet_timer():
    global bulletIsFired
    global bomberlist

    if bulletIsFired == 1:
        bullet1.forward(20)
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


def gameover():
    global wn
    global gameoverstate
    gameoverstate=1
    turtle.color("red")
    style = ('Times', 30, 'italic')
    turtle.penup()
    turtle.hideturtle()
    turtle.setpos(0,-350)
    turtle.write('Game Over! Press Escape to Exit', font=style, align='center')
    turtle.hideturtle()
    turtle.onkey(None, "Right")
    turtle.onkey(None, "Left")
    turtle.onkey(None, "space")



def turtleend():
    wn.bye()

# Setup Turtle

turtle.listen()
turtle.onkey(turn_right, "Right")
turtle.onkey(turn_left, "Left")
turtle.onkey(shoot_bullet, "space")
turtle.onkey(turtleend, "Escape")

timer()

turtle.mainloop()
