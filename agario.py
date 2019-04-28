import turtle as t
import random as r
import time
import threading
from move import move
from killiing_ball import killing
from food import contacts_with_objects as cko
from objects import agario_obj as a, boost_obj as b, food_obj as f, killing_obj as k


#main window
s = 0.4                                 #### agario speed
wn = t.Screen()
wn.title("agario game")
wn.setup(width=600, height=500)
wn.tracer(0)
wn.bgcolor("black")



while True:

    wn.update()
    move(a.agario_object, wn, s).movement() ### movement part
    killing(k.killing_object, a.agario_object,k.killing_ball).agario_border_check(), killing(k.killing_object, a.agario_object,k.killing_ball).killing_ball_check() ## kiling balls part
    cko(a.agario_object,f.food_object, f.food).food_con(), cko(a.agario_object,f.food_object, f.food).boost_con(b.boost_object, b.boost) ## contacts part
    


wn.mainloop()
