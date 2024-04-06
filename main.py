from tkinter import *
from random import randint
from math import pi, cos, sin

window = Tk()
window.title('Sierpinski')

W, H = 600, 600
DELAY = 5
N_POINTS = 3

canvas = Canvas( window, width = W, height = H )
canvas.pack(expand=YES, fill=BOTH)

class Circle():
    def __init__(self, centerX, centerY, radius, color="black", temp = False):
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius
        fill = ""
        tag = ""
        if color != "black":
            fill = color
        if temp:
            tag = "temp"

        canvas.create_oval(
            centerX - radius, 
            centerY - radius, 
            centerX + radius,
            centerY + radius,
            width = 5,
            outline = color,
            fill = fill,
            tags = tag
        )

bigCircle = Circle(W / 2, H / 2, 200)
randomPoints = [x for x in range(N_POINTS)]

for x in randomPoints:
    theta = x * (360 / N_POINTS) * pi / 180
    x = bigCircle.centerX + bigCircle.radius * cos(theta)
    y = bigCircle.centerY + bigCircle.radius * sin(theta)
    Circle(x, y, 1, color="blue")


def FindRandomPointInCircle(circle = Circle):
    global randomPoints
    theta = randomPoints[randint(0, N_POINTS - 1)] * (360 / N_POINTS) * pi / 180
    x = circle.centerX + circle.radius * cos(theta)
    y = circle.centerY + circle.radius * sin(theta)
    return x, y

lastPosX, lastPosY = W / 2, H / 2

def drawSierpinski():
    global lastPosX, lastPosY

    # Create last circle
    Circle(lastPosX, lastPosY, 0.1)

    # Delete all temporary items
    canvas.delete("temp")

    # Choose a random point at the circumference
    randX, randY = FindRandomPointInCircle(bigCircle)

    # Create a line conecting the last point and the chosen point
    canvas.create_line(lastPosX, lastPosY, randX, randY, fill="purple", width=3, tags="temp")
    Circle(lastPosX, lastPosY, 1, "blue", temp = True)
    Circle(randX, randY, 1, "blue", temp = "True")

    # Update the last point to be the point at the middle of the line
    lastPosX = (lastPosX + randX) / 2.0
    lastPosY = (lastPosY + randY) / 2.0
    canvas.after(DELAY, drawSierpinski)

canvas.after(DELAY, drawSierpinski)

window.mainloop()
