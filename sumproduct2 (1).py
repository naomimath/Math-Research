#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This step prompts the user to enter 2 integer inputs
# These inputs are used to define the dimensions of the sum product table

print("Enter integers for x and y to generate the table")
print("\n")

x = input("First enter an integer value for x = ")
print("\n")

y = input("Now enter an integer value for y = ")
print("\n")

print(x)
print("\n")

print(y)
print("\n")

x = int(x)
y = int(y)


# In[2]:


import math

# This step calculates side a, which is the height of the right triangle used for factorization
# A 2D-array is used, since a is a function of x and y
# Note: 1 is added to both j and i, because i and j are both initialized at 0

rows, cols = (x, y)
arr_a = []
for i in range(rows):
    col = []
    for j in range(cols):
        a = math.sqrt((i + 1) * (j + 1))
        col.append(a)
    arr_a.append(col)
print(arr_a)

# This step calculates side b, which is the base of the right triangle used for factorization
# A 2D-array is used, since b is a function of x and y

rows, cols = (x, y)
arr_b = []
for i in range(rows):
    col = []
    for j in range(cols):
        b = abs((i - j) / 2)
        col.append(b)
    arr_b.append(col)
print(arr_b)

# This step calculates side c, which is the hypotenuse of the right triangle used for factorization
# A 2D-array is used, since c is a function of x and y
# Note: 1 is added to both j and i, because i and j are both initialized at 0

rows, cols = (x, y)
arr_c = []
for i in range(rows):
    col = []
    for j in range(cols):
        c = (i + j + 2) / 2
        col.append(c)
    arr_c.append(col)
print(arr_c)

# This step calculates a^2, which will be used to display the exact value of xy (not decimal)
# A 2D-array is used, since a^2 is a function of x and y
# Note: 1 is added to both j and i, because i and j are both initialized at 0

rows, cols = (x, y)
arr_a2 = []
for i in range(rows):
    col = []
    for j in range(cols):
        a2 = (i + 1) * (j + 1)
        col.append(a2)
    arr_a2.append(col)
print(arr_a2)

# This step calculates t, which represents theta in the right triangle
# A 2D-array is used, since t is a function of b and c
# 90 degree values occur at perfect squares

rows, cols = (x, y)
arr_t = []
for i in range(rows):
    col = []
    for j in range(cols):
        
        b = arr_b[i][j]
        c = arr_c[i][j]
        t = math.acos(b / c)
        t = math.degrees(t)
        
        col.append(t)   
    arr_t.append(col)
print(arr_t)


# In[ ]:


# This step imports the turtle library
# The turtle library will be used to visually represent the table
# We initialize the openScreen variable to open the window
# The window will be used to create graphics
# We initialize the my_t variable, which acts as a pen, referred to as the turtle

import turtle

openScreen = turtle.getscreen()
my_t = turtle.Turtle()

# This step sets the turtle to the max speed
# The penup function allows us to move the turtle without drawing
# We move the turtle to the top left of the screen to conserve space
# The penup function allows us to draw again
# I also added some code (from stackoverflow) to disable screen refreshing so it speeds turtle up
# Not too sure how it works but I'm reading up on it

import random
import time

my_t.speed(0)

screen = turtle.Screen()
screen.screensize(y * 200, x * 200)

turtlepower = []

turtle.tracer(0, 0)

my_t.penup()
my_t.goto(-650,400)
my_t.pendown()

# This step begins drawing the table, with x rows and y columns
# We draw empty squares before adding any other information

from turtle import *

for i in range(x):
    my_t.right(90)
    my_t.forward(100)
    my_t.left(90)
    for j in range(y):
        for k in range(4):
           my_t.forward(100)
           my_t.left(90)
            
        my_t.forward(100)
    my_t.backward(100*y)
    
my_t.penup()
my_t.goto(-625, 425)
my_t.pendown()
my_t.write("input y:", font=("Arial", 18, "normal"))

my_t.penup()
my_t.goto(-710, 375)
my_t.pendown()
my_t.write("input x:", font=("Arial", 18, "normal"))

my_t.penup()

# This step draws each x, y pair's unique right triangle
# No right triangle exists when x = y

my_t.penup()

for i in range(x):
    y_coord = 390 - (i * 100)
    for j in range(y):
        x_coord = -630 + (j * 100)
        
        d_theta = arr_t[i][j]
        r_theta = math.radians(d_theta)
        side_a = 60 * math.sin(r_theta)
        side_b = 60 * math.cos(r_theta)
        
        my_t.color("purple")
        my_t.penup()
        my_t.goto(x_coord - 4, y_coord - 1)
        my_t.pendown()
        my_t.write("\u03B8")
        my_t.penup()
        
        my_t.goto(x_coord, y_coord)
        my_t.pendown()
        
        my_t.right(90)
        my_t.color("red")
        my_t.forward(side_a)
        my_t.color("blue")
        my_t.left(90)
        my_t.forward(side_b)
        my_t.color("green")
        my_t.left(180 - d_theta)
        my_t.forward(60)
        my_t.color("black")
        
        my_t.penup()
        my_t.right(180 - d_theta)
        
# This step populates each element of the table with its right trangle values

my_t.penup()

for i in range(x):
    y_coord = 320 - (i * 100)
    for j in range(y):
        x_coord = -640 + (j * 100)
        
        a = str(round(arr_a[i][j], 2))
        b = str(round(arr_b[i][j], 2))
        c = str(round(arr_c[i][j], 2))
        theta = str(round((90 - arr_t[i][j]), 2))
        
        my_t.goto(x_coord, y_coord)
        my_t.pendown()
        
        my_t.color("red")
        my_t.write("a = ")
        my_t.color("black")
        my_t.penup()
        my_t.goto(x_coord + 14, y_coord)
        my_t.pendown()
        my_t.write(a)
        
        my_t.penup()
        my_t.goto(x_coord, y_coord - 10)
        my_t.pendown()
        
        my_t.color("blue")
        my_t.write("b = ")
        my_t.color("black")
        my_t.penup()
        my_t.goto(x_coord + 14, y_coord - 10)
        my_t.pendown()
        my_t.write(b)
        
        my_t.penup()
        my_t.goto(x_coord + 40, y_coord)
        my_t.pendown()
        
        my_t.color("green")
        my_t.write("c = ")
        my_t.color("black")
        my_t.penup()
        my_t.goto(x_coord + 40 + 14, y_coord)
        my_t.pendown()
        my_t.write(c)
        
        my_t.penup()
        my_t.goto(x_coord + 40, y_coord - 10)
        my_t.pendown()
        
        my_t.color("purple")
        my_t.write("\u03B8")
        my_t.color("black")
        my_t.penup()
        my_t.goto(x_coord + 40 + 4, y_coord - 10)
        my_t.pendown()
        my_t.write(" = ")
        my_t.penup()
        my_t.goto(x_coord + 40 + 14, y_coord - 10)
        my_t.pendown()
        my_t.write(theta) 
          
        my_t.penup()
        
# This step labels the x and y values for the rows and columns

for i in range(x):
    my_t.goto(-660, 350 - (i*100))
    my_t.pendown()
    my_t.write(i + 1, font=("Arial", 12, "normal"))
    my_t.penup()
    
for j in range(y):
    my_t.goto(-600 + (j*100), 405)
    my_t.pendown()
    my_t.write(j + 1, font=("Arial", 12, "normal"))
    my_t.penup()
    
# This step labels all of elements with a theta value of 70.53

for i in range(1, x, 2):
    j = i//2
    my_t.goto(-650 + (100 * j), 400 - (100 * i))
    my_t.pendown()
    my_t.color("yellow")
    my_t.pensize(3)
    for k in range(4):
        my_t.forward(100)
        my_t.right(90)
    my_t.penup()

for i in range(1, y, 2):
    j = i//2
    my_t.goto(-650 + (100 * i), 400 - (100 * j))
    my_t.pendown()
    my_t.color("yellow")
    my_t.pensize(3)
    for k in range(4):
        my_t.forward(100)
        my_t.right(90)
    my_t.penup()
    
# This step labels all of elements with a theta value of 60

for i in range(2, x, 3):
    j = i//3
    my_t.goto(-650 + (100 * j), 400 - (100 * i))
    my_t.pendown()
    my_t.color("orange")
    my_t.pensize(3)
    for k in range(4):
        my_t.forward(100)
        my_t.right(90)
    my_t.penup()
    
# This step is a continuation of the previous step

for i in range(2, y, 3):
    j = i//3
    my_t.goto(-650 + (100 * i), 400 - (100 * j))
    my_t.pendown()
    my_t.color("orange")
    my_t.pensize(3)
    for k in range(4):
        my_t.forward(100)
        my_t.right(90)
    my_t.penup()
    
# This step labels all of elements with a theta value of 53.13

for i in range(3, x, 4):
    j = i//4
    my_t.goto(-650 + (100 * j), 400 - (100 * i))
    my_t.pendown()
    my_t.color("pink")
    my_t.pensize(3)
    for k in range(4):
        my_t.forward(100)
        my_t.right(90)
    my_t.penup()
    

for i in range(3, y, 4):
    j = i//4
    my_t.goto(-650 + (100 * i), 400 - (100 * j))
    my_t.pendown()
    my_t.color("pink")
    my_t.pensize(3)
    for k in range(4):
        my_t.forward(100)
        my_t.right(90)
    my_t.penup()
    
# This step labels all of elements with a theta value of 48.19

for i in range(4, x, 5):
    j = i//5
    my_t.goto(-650 + (100 * j), 400 - (100 * i))
    my_t.pendown()
    my_t.color("purple")
    my_t.pensize(3)
    for k in range(4):
        my_t.forward(100)
        my_t.right(90)
    my_t.penup()

for i in range(4, y, 5):
    j = i//5
    my_t.goto(-650 + (100 * i), 400 - (100 * j))
    my_t.pendown()
    my_t.color("purple")
    my_t.pensize(3)
    for k in range(4):
        my_t.forward(100)
        my_t.right(90)
    my_t.penup()
    
# This step labels all of elements with a theta value of 44.42

for i in range(5, x, 6):
    j = i//6
    my_t.goto(-650 + (100 * j), 400 - (100 * i))
    my_t.pendown()
    my_t.color("green")
    my_t.pensize(3)
    for k in range(4):
        my_t.forward(100)
        my_t.right(90)
    my_t.penup()

for i in range(5, y, 6):
    j = i//6
    my_t.goto(-650 + (100 * i), 400 - (100 * j))
    my_t.pendown()
    my_t.color("green")
    my_t.pensize(3)
    for k in range(4):
        my_t.forward(100)
        my_t.right(90)
    my_t.penup()
    
# This step labels all of elements with a theta value of 41.41

for i in range(6, x, 7):
    j = i//7
    my_t.goto(-650 + (100 * j), 400 - (100 * i))
    my_t.pendown()
    my_t.color("blue")
    my_t.pensize(3)
    for k in range(4):
        my_t.forward(100)
        my_t.right(90)
    my_t.penup()

for i in range(6, y, 7):
    j = i//7
    my_t.goto(-650 + (100 * i), 400 - (100 * j))
    my_t.pendown()
    my_t.color("blue")
    my_t.pensize(3)
    for k in range(4):
        my_t.forward(100)
        my_t.right(90)
    my_t.penup()
    
# This step labels all of elements with a theta value of 38.94

for i in range(7, x, 8):
    j = i//8
    my_t.goto(-650 + (100 * j), 400 - (100 * i))
    my_t.pendown()
    my_t.color("red")
    my_t.pensize(3)
    for k in range(4):
        my_t.forward(100)
        my_t.right(90)
    my_t.penup()

for i in range(7, y, 8):
    j = i//8
    my_t.goto(-650 + (100 * i), 400 - (100 * j))
    my_t.pendown()
    my_t.color("red")
    my_t.pensize(3)
    for k in range(4):
        my_t.forward(100)
        my_t.right(90)
    my_t.penup()
    
# This step stops the turtle

turtle.update()
time.sleep(3)
turtle.done()


# In[ ]:





# In[ ]:




