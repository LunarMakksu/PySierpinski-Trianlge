import turtle
import random
import numpy as np
import time

t = turtle.Turtle()
turtle.bgcolor('black')

t.speed(5)
t.hideturtle()
t.showturtle()

t.pencolor("white")
turtle.bgcolor("black")
t.pensize(7)
screen = turtle.Screen()
#screen.screensize(600, 900)

point1 = (-200, -300)
point2 = (200, -300)
point3 = (0, 300)

t.penup()
t.goto(point1)
t.pendown()
t.forward(0.01)
t.penup()
t.goto(point2)
t.pendown()
t.forward(0.01)
t.penup()
t.goto(point3)
t.pendown()
t.forward(0.01)
t.penup()
t.pensize(1)
t.speed(0)

counter = 0

random_width = np.arange(-201, 200, 0.01).tolist()
random_height = np.arange(-301, 300, 0.01).tolist()
all_points = (point1, point2, point3)

point_W = random.choice(random_width)
point_H = random.choice(random_height)
point = (point_W, point_H)
t1 = time.time()
t.goto(point_H, point_H)
t.pendown()
t.forward(0.01)
t.penup()
base_point = random.choice(all_points)
t.goto(point_W + ((base_point[0]-point_W)/2), ((point_H - base_point[1])/2) + base_point[1])
t.pendown()
t.forward(0.01)
t.penup()
counter += 1


def choose_point(prev_w, prev_h):
    base_point = random.choice(all_points)
    new_point_w = prev_w + ((base_point[0]-prev_w)/2)
    new_point_h = ((prev_h - base_point[1])/2) + base_point[1]
    t.goto(new_point_w, new_point_h)
    t.pendown()
    t.forward(0.01)
    t.penup()
    return (new_point_w, new_point_h)

(prev_W, prev_H) = choose_point(point_W + ((base_point[0]-point_W)/2), ((point_H - base_point[1])/2) + base_point[1])

while (counter < 25000):
    (prev_W, prev_H) = choose_point(prev_W, prev_H)
    counter += 1
    if (counter % 1000) == 0:
        t3 = time.time()
        print(f"{counter} points on screen at {round((t3-t1)/60, 3)} minutes")

t2=time.time()
print(f"\nFinsished! With {counter} points on screen. Time taken: {(t2-t1)/60} minutes")
t.hideturtle()
screen.exitonclick()
