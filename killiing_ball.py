import random as r 


class killing():
    dist = 20
    boost_count = 0
    def __init__(self, killing_object, agario, list):
        self.killing_object= killing_object
        self.agario = agario
        self.list = list
        
        
        
        
    def killing_ball_check(self):
        for self.killing_object in self.list: ### object and list
        #killing ball movement
            self.killing_object.setx(self.killing_object.xcor() + self.killing_object.dx)
            self.killing_object.sety(self.killing_object.ycor() + self.killing_object.dy)
        #killing ball border check
            if self.killing_object.xcor() > 290:
                self.killing_object.setx(290)
                self.killing_object.dx *= -1
            if self.killing_object.xcor() < -290:
                self.killing_object.setx(-290)
                self.killing_object.dx *= -1
            if self.killing_object.ycor() > 240:
                self.killing_object.sety(240)
                self.killing_object.dy *= -1
            if self.killing_object.ycor() < -240:
                self.killing_object.sety(-240)
                self.killing_object.dy *= -1
        #killing ball contact with agario
            if self.boost_count == 0:
                self.agario.color('red')
                if self.killing_object.distance(self.agario) < self.dist:
                    killing.dist = 20
                    self.agario.goto(0,0)
                    self.agario.direction = "stop"
                    self.agario.turtlesize(1, 1, 1)
            if self.boost_count != 0:
                pass
                
    
    def agario_border_check(self):
        #border check
        if self.agario.ycor() > 250:
            killing.dist = 20
            self.agario.goto(0,0)
            self.agario.direction = "stop"
            self.agario.turtlesize(1, 1, 1)
        if self.agario.ycor() < -250:
            killing.dist = 20
            self.agario.goto(0,0)
            self.agario.direction = "stop"
            self.agario.turtlesize(1, 1, 1)
        if self.agario.xcor() > 300:
            killing.dist = 20
            self.agario.goto(0,0)
            self.agario.direction = "stop"
            self.agario.turtlesize(1, 1, 1)
        if self.agario.xcor() < -300:
            killing.dist = 20
            self.agario.direction = "stop"
            self.agario.turtlesize(1, 1, 1)
            self.agario.goto(0,0)
    
   
    
    