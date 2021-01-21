import turtle
from random import *
from turtle import *

penup()
goto(-140,140) 

for sp in range(15): 
  speed(10)
  write(sp)
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)


tospa = Turtle() 
tospa.color('green') 
tospa.shape('turtle') 
tospa.penup() 
tospa.goto(-160,100) 
tospa.pendown() 


kaplumbağa = Turtle() 
kaplumbağa.color('red') 
kaplumbağa.shape('turtle') 
kaplumbağa.penup() 
kaplumbağa.goto(-160,80)
kaplumbağa.pendown() 

karpuzcu = Turtle() 
karpuzcu.color('blue') 
karpuzcu.shape('turtle') 
karpuzcu.penup()
karpuzcu.goto(-160,60) 
karpuzcu.pendown() 

bejo = Turtle() 
bejo.color('black') 
bejo.shape('turtle') 
bejo.penup() 
bejo.goto(-160,40) 
bejo.pendown() 

kavuncu = Turtle() 
kavuncu.color('yellow') 
kavuncu.shape('turtle') 
kavuncu.penup() 
kavuncu.goto(-160,20) 
kavuncu.pendown()

lord = Turtle() 
lord.color('aqua') 
lord.shape('turtle') 
lord.penup() 
lord.goto(-160,0) 
lord.pendown() 

for turn in range(100): 
  tospa.forward(randint(1,5))
  kaplumbağa.forward(randint(1,5)) 
  karpuzcu.forward(randint(1,5))
  bejo.forward(randint(1,5))
  kavuncu.forward(randint(1,5))
  lord.forward(randint(1,5))

turtle.done()