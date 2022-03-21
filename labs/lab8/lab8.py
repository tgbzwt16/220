from random import randint
from time import sleep
import random
import math
from graphics import *


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = color_rgb(r, g, b)
    return rgb


def get_random(x):
    return randint(-x, x)


def hit_vertical(car, win):
    center = car.getCenter()
    x = center.getX()
    radius = car.getRadius()
    width = win.getWidth()
    if x <= radius or x >= width-radius:
        return True
    else:
        return False


def hit_horizontal(car, win):
    center = car.getCenter()
    x = center.getY()
    radius = car.getRadius()
    height = win.getHeight()
    if x <= radius or x >= height-radius:
        return True
    else:
        return False


def collided(car1, car2):
    rad1 = car1.getRadius()
    rad2 = car2.getRadius()
    center1 = car1.getCenter()
    center2 = car2.getCenter()

    x1 = center1.getX()
    x2 = center2.getX()
    y1 = center1.getY()
    y2 = center2.getY()

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    radius_total = rad1 + rad2

    return bool(radius_total >= distance)


def bumper_car():
    width = 800
    height = 800
    win = GraphWin("Clicks", width, height)
    win.setBackground("white")

    car1 = Circle(Point(200, 200), 50)
    car1.setOutline("black")
    car1.setFill(get_random_color())
    car1.draw(win)

    car2 = Circle(Point(400, 350), 50)
    car2.setOutline("black")
    car2.setFill(get_random_color())
    car2.draw(win)

    x1 = get_random(20)
    x2 = get_random(20)
    y1 = get_random(20)
    y2 = get_random(20)

    for i in range(500):
        sleep(.02)
        car1.move(x1, y1)
        car2.move(x2, y2)
        if hit_vertical(car1, win):
            x1 = x1 * -1
        if hit_vertical(car2, win):
            x2 = x2 * -1
        if hit_horizontal(car1, win):
            y1 = y1 * -1
        if hit_horizontal(car2, win):
            y2 = y2 * -1
        if collided(car1, car2):
            x1 = x1 * -1
            x2 = x2 * -1
            y1 = y1 * -1
            y2 = y2 * -1

    msg = Text(Point(400, 400), 'Click anywhere to close')
    msg.setSize(25)
    msg.draw(win)
    win.getMouse()
    win.close()





