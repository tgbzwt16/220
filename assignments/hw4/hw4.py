"""
Name: Thomas Thornley
hw4.py

Problem: Creating visual programs and approximating pi in a new way

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

import math
from graphics import *


def squares():

    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    num_clicks = 5

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw square")
    instructions.draw(win)

    shape = Rectangle(Point(50, 50), Point(20, 20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()

        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()

        shape2 = Rectangle(Point(50, 50), Point(20, 20))
        shape2.setOutline("red")
        shape2.setFill("red")
        shape2.draw(win)
        shape2.move(change_x, change_y)

    msg = Text(Point(200, 200), 'Click again to close')
    msg.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    click1 = win.getMouse()
    x1 = click1.getX()
    y1 = click1.getY()
    click2 = win.getMouse()
    x2 = click2.getX()
    y2 = click2.getY()

    shape = Rectangle(Point(x1, y1), Point(x2, y2))
    shape.setOutline('black')
    shape.setFill('green')
    shape.draw(win)

    area = (x2 - x1) * (y2 - y1)
    perimeter = (2 * (x2 - x1)) + (2 * (y2 - y1))

    inst_pt1 = Point(width / 2, height - 30)
    instructions1 = Text(inst_pt1, "Perimeter: " + str(abs(perimeter)))
    instructions1.draw(win)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Area: " + str(abs(area)))
    instructions.draw(win)

    msg = Text(Point(200, 200), 'Click again to close')
    msg.draw(win)
    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    click1 = win.getMouse()
    x1 = click1.getX()
    y1 = click1.getY()

    click2 = win.getMouse()
    x2 = click2.getX()
    y2 = click2.getY()

    x_total = (x2 - x1) ** 2
    y_total = (y2 - y1) ** 2
    distance = (x_total + y_total) ** (1/2)

    shape = Circle(click1, distance)
    shape.setOutline("black")
    shape.setFill("light blue")
    shape.draw(win)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "radius: " + str(distance))
    instructions.draw(win)

    msg = Text(Point(200, 200), 'Click again to close')
    msg.draw(win)
    win.getMouse()
    win.close()


def pi2():
    terms = eval(input('Enter the number of terms to sum: '))
    den = 1
    pi = 0
    sign = 1
    for i in range(terms):
        pi += 4 / den * sign
        den += 2
        sign = sign * -1
        i -= 1
    print(pi)
    print(abs(math.pi - pi))
