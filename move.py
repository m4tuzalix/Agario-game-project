import turtle as t 
import random as r 


class move():
    def __init__(self, agario, window, speed):
        self.agario = agario
        self.window = window
        self.speed = speed
    def movement(self):
        if self.agario.direction == "up":
            y = self.agario.ycor()
            y += self.speed
            self.agario.sety(y)
        if self.agario.direction == "down":
            y = self.agario.ycor()
            y -= self.speed
            self.agario.sety(y)
        if self.agario.direction == "left":
            x = self.agario.xcor()
            x -= self.speed
            self.agario.setx(x)
        if self.agario.direction == "right":
            x = self.agario.xcor()
            x += self.speed
            self.agario.setx(x)
        self.bind()

    def go_up(self):
        if self.agario.direction != "down":
            self.agario.direction = "up"
    def go_down(self):
        if self.agario.direction != "up":
            self.agario.direction = "down"
    def go_left(self):
        if self.agario.direction != "right":
            self.agario.direction = "left"
    def go_right(self):
        if self.agario.direction != "left":
            self.agario.direction = "right"

    def bind(self):
        self.window.listen()
        self.window.onkeypress(self.go_up, "w" )
        self.window.onkeypress(self.go_down, "s" )
        self.window.onkeypress(self.go_left, "a" )
        self.window.onkeypress(self.go_right, "d" )