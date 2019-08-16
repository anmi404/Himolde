#!/usr/bin/env python3.7 
#Demonstrates: conditionals (and/or), loops, range, functions

#create screen and head. capture keyboard. Move the head 
#detect collision with fruit. Move fruit to random position.Grow body
#prevent the head to collide with the border
#prevent the head to turn back
#prevent the head to collide with own body
#scores

import turtle
import time #for delay
import random #move food after collision

delay = 0.2
segments = []

#set up screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("light yellow")
window.setup(height=600, width=600) #Better use window.window_height(), window.window_width()

#score
window.score = 0
window.high_score = 0

#score pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
#not drawing lines
pen.penup()
pen.hideturtle()
pen.goto(0,window.window_width()/2-35) #width = 260
pen.write("Score: 0 High Score: 0", align = "center", font = ("Courier", 24, "normal")  )

#turning animation off on the screen
window.tracer(0)

#snake head: turtle object
head = turtle.Turtle()
#turtles are 20 x 20 pixels by default
head.speed(0)
head.shape("square")
head.fillcolor("black") #light green
#don't draw
head.penup()
#starts in the center
head.home()
head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20) #too fast without the delay (time module)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20) #too fast without the delay (time module)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20) #too fast without the delay (time module)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20) #too fast without the delay (time module)

def return_to_center():
    time.sleep(1)

    #clear score
    window.score = 0
    print(window.score)
    pen.clear() #otherwise it will overwrite itself
    #format substitute the braces {}
    pen.write("Score: {} High Score: {}".format(window.score, window.high_score), align = "center", font = ("Courier", 24, "normal"))  

    #hide body
    for segment in segments:
        if segment!=head:
            segment.hideturtle()
            segment.clear()
            
    segments.clear()
    segments.append(head)
    head.home() 
    head.direction = "stop"


def go_up():
    if head.direction=="down":
        return_to_center()
    head.direction = "up"
def go_down():
    if head.direction=="up":
        return_to_center()
    head.direction = "down"
def go_left():
    if head.direction=="right":
        return_to_center()
    head.direction = "left"
def go_right ():
    if head.direction=="left":
        return_to_center()
    head.direction = "right"


#Keyboard bindings
window.listen() #listen for keypresses
window.onkeypress(go_up, key="Up")
window.onkeypress(go_down, key="Down")
window.onkeypress(go_left, key="Left")
window.onkeypress(go_right, key="Right")

#snake food 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
x = random.randint(-280, 280)
y = random.randint( -280, 280)
food.goto(x,y)

segments.append(head)

while True:
    window.update()
    #move()

    if head.distance(food) <= 20:
        #collision! Move the food to a random spot
        #center is 0,0, 290 because it measures 10 radius, 299 would leave the screen
        x = random.randint(-280, 280)
        y = random.randint( -280, 280)
        food.goto(x,y)

        #After the collision add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        #new_segment.fillcolor("gray")
        new_segment.color("gray")
        new_segment.penup()
        new_segment.goto(0, 100)
        new_segment.penup()
        segments.append(new_segment)

        #increase score
        print(window.score)
        window.score += 10

        if window.score > window.high_score:
            window.high_score = window.score

        #pen update (May be a function)
        pen.clear() #otherwise it will overwrite itself
        #format substitute the braces {}
        pen.write("Score: {} High Score: {}".format(window.score, window.high_score), align = "center", font = ("Courier", 24, "normal"))  
        
    #Move all segments, starting by the last one to the position where the previous one was
    #len(segments)-1 => lists start at zero
    #stops at 1 (not inclusive)
    # -1 => down by 1 each time
    #xcoordinates, each segment is a turtle
    for i in range (len(segments)-1, 0, -1):
        x0 = head.xcor() 
        y0 = head.ycor()
        x = segments[i-1].xcor() 
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    move()    

    if (head.xcor() <= -290 or head.xcor() >= 290 or head.ycor() <= -290 or head.ycor() >= 290):
        return_to_center()

    #head collision
    for segment in segments:
        if segment!=head and segment.distance(head) == 0:
            #collision
            return_to_center()

    time.sleep(delay)

turtle.mainloop()    


# from turtle import Turtle, Screen

# screen = Screen()

# screen.setup(500, 500)
# screen.title("Turtle Keys")

# move = Turtle(shape="turtle")

# def k1():
#     move.forward(10)

# def k2():
#     move.left(45)

# def k3():
#     move.right(45)

# def k4():
#     move.backward(10)

# screen.onkey(k1, "Up")
# screen.onkey(k2, "Left")
# screen.onkey(k3, "Right")
# screen.onkey(k4, "Down")

# screen.listen()

# screen.exitonclick()