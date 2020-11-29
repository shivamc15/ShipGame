import turtle

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
            self.bturtle.forward(1)

    def istouchingBullet(self, bullet):
        bulletpos = bullet.pos()
        return self.bturtle.distance(bulletpos[0], bulletpos[1]) < 15

    def ishittingship(self):
        return self.bturtle.distance(0, 0) < 15

