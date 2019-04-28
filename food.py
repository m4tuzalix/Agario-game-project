from killiing_ball import killing
import random as r
import threading
import time
import turtle as t

class contacts_with_objects():
    
    def __init__(self, agario, obj, lis):
        self.agario = agario
        self.obj = obj
        self.lis = lis
       
        
    
    def food_con(self):
        #contact with food
        for self.obj in self.lis:
            if self.agario.distance(self.obj) < killing.dist: ### dist means distance and as a default is set to 20
                killing.dist = killing.dist + 1
                x = r.randint(-290, 290)
                y = r.randint(-240, 240)
                self.obj.goto(x,y)
                self.grow()
                print(killing.dist)
    def grow(self):
        grow1  = self.agario.turtlesize()
        increase = tuple([0.1 + num for num in grow1])
        self.agario.turtlesize(*increase)
        print(increase)

    def timer(self):
        for x in range(10):
            time.sleep(1)
            if x==9:
                killing.boost_count = 0
                    

    def boost_con(self, boost_object, boost_list):
        self.boost_object = boost_object
        self.boost_list = boost_list
        for self.boost_object in self.boost_list:
            if self.agario.distance(self.boost_object) < killing.dist:
                killing.dist = killing.dist
                killing.boost_count += 1
                x = r.randint(-290, 290)
                y = r.randint(-240, 240)
                self.boost_object.goto(x,y)
                self.thr = threading.Thread(target=self.timer)
                self.thr.start()
                self.agario.color('yellow')
                
    
            
        
                
                

    

    