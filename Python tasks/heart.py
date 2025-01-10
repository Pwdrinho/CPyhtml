import math  #importa a biblioteca math
import turtle #importa a biblioteca turtle
from turtle import *
def heart(k): 
    return 9*math.sin(k)**3
def heart1(k):
    return 9*math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)
speed(250) #velocidade da tartaruga
color('red') #cor da tartaruga
for i in range(600): 
    goto(heart(i)*23, heart1(i)*23)
for j in range(600):
    color('red')