import random as r 
import turtle as t 
import threading
import time
class agario_obj():
    #agario object
    agario_object = t.Turtle()
    agario_object.shape("circle")
    agario_object.color("red")
    agario_object.turtlesize()
    agario_object.speed(0)
    agario_object.penup()
    agario_object.goto(0,0)
    agario_object.direction = "stop"

class boost_obj():
    boost = []
    boost_object = t.Turtle()
    boost_object.shape("square")
    boost_object.turtlesize(0.8,0.8,0.8)
    boost_object.color("yellow")
    boost_object.speed(0)
    boost_object.penup()
    x = r.randint(-290, 290)
    y = r.randint(-240, 240)
    boost_object.goto(x, y)
    boost.append(boost_object)
    
class food_obj():
    food = []
    for _ in range(4):
        food_object = t.Turtle()
        food_object.shape("square")
        food_object.turtlesize(0.8,0.8,0.8)
        food_object.color("green")
        food_object.speed(0)
        food_object.penup()
        x = r.randint(-290, 290)
        y = r.randint(-240, 240)
        food_object.goto(x, y)
        food.append(food_object)

class killing_obj():
    kb_speed = 0.4
    killing_ball = []
    for _ in range(3):
        killing_object = t.Turtle()
        killing_object.shape("circle")
        killing_object.color("white")
        killing_object.speed(0)
        killing_object.penup()
        x = r.randint(-290, 290)
        y = r.randint(-240, 240)
        killing_object.goto(x, y)
        killing_object.dx = kb_speed
        killing_object.dy = kb_speed
        killing_ball.append(killing_object)
    