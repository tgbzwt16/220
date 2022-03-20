"""
Name: thomas thornley
hw8.py

Problem: writing conditional functions

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

import math
from graphics import Circle, GraphWin, Text, Point


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]


def sum_list(nums):
    acc = 0
    for i in nums:
        if type(i) == int:
            acc = acc + int(i)
        else:
            acc = acc + float(i)
    return acc


def to_numbers(nums):
    for i in range(0, len(nums)):
        nums[i] = eval(nums[i])


def sum_of_squares(nums):
    total =[]
    for i in range(len(nums)):
        nums[i] = nums[i].split(',')
        to_numbers(nums[i])
        square_each(nums[i])
        total.append(sum_list(nums[i]))
    return total


def starter(weight, wins):
    if weight >= 150 and weight < 160 and wins >= 5:
        return True
    return bool(weight > 199 and wins > 20)


def leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    return bool((year % 4 ==0) and (year % 100 != 0))


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    win.setBackground("white")
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center1 = win.getMouse()
    circumference_point1 = win.getMouse()
    radius1 = math.sqrt(
        (center1.getX() - circumference_point1.getX()) ** 2 + (center1.getY() - circumference_point1.getY()) ** 2)
    circle_one1 = Circle(center1, radius1)
    circle_one1.setFill("light green")
    circle_one1.draw(win)

    did_overlap(circle_one, circle_one1)

    msg = Text(Point(width_px / 2, height_px / 2), 'Click again to close')
    msg.draw(win)
    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    rad1 = circle_one.getRadius()
    rad2 = circle_two.getRadius()
    center1 = circle_one.getCenter()
    center2 = circle_two.getCenter()

    x1 = center1.getX()
    x2 = center2.getX()
    y1 = center1.getY()
    y2 = center2.getY()

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    radius_total = rad1 + rad2

    return bool(radius_total >= distance)


