from turtle import *
import turtle
import sys
import keyboard
def draw():
    Colors = ['red','green','yellow','purple','violet','blue']
    t = turtle.Pen()
    t.speed(10)
    turtle.bgcolor('black')
    for i in range(500):
        t.pencolor(Colors[i%6])
        t.width(i/100+1)
        t.forward(i)    
        t.left(55)
    turtle.done()
    ontimer(stop, 500)

if __name__ == "__main__":
    if keyboard.is_pressed('Esc'):
        sys.exit()
    draw()

