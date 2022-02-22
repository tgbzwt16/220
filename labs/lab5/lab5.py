from graphics import *
import math


def triangle():
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    click1 = win.getMouse()
    x1 = click1.getX()
    y1 = click1.getY()
    click2 = win.getMouse()
    x2 = click2.getX()
    y2 = click2.getY()
    click3 = win.getMouse()
    x3 = click3.getX()
    y3 = click3.getY()

    shape = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    shape.setOutline('white')
    shape.setFill('blue')
    shape.draw(win)

    side_a = math.sqrt((abs(x2 - x3) ** 2) + (abs(y2 - y3) ** 2))
    side_b = math.sqrt((abs(x1 - x3) ** 2) + (abs(y1 - y3) ** 2))
    side_c = math.sqrt((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2))

    perimeter = side_a + side_b + side_c
    s = perimeter / 2
    area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))

    inst_pt1 = Point(width / 2, height - 30)
    instructions1 = Text(inst_pt1, "Perimeter: " + str(abs(perimeter)))
    instructions1.draw(win)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Area: " + str(area))
    instructions.draw(win)


def color_shape():
    # Create code to allow a user to color a shape by entering rgb amounts

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    input_box = Entry(red_text_pt, 5)
    input_box.draw(win)
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    input_box = Entry(green_text_pt, 5)
    input_box.draw(win)
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    input_box = Entry(blue_text_pt, 5)
    input_box.draw(win)
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    input_box = Entry(red_text_pt, 10)
    input_box.draw(win)


    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string = input('enter a string: ')
    ten_times = ''
    first_letter = string[0]
    last_letter = string[-1]
    two_five = string[1:6]
    first_last = string[0] + string[-1]
    for j in range(10):
        ten_times += string[0:3]

    print(first_letter)
    print(last_letter)
    print(two_five)
    print(first_last)
    print(ten_times)
    for x in string:
        print(x)
    print(len(string))


def process_list():
    pt = Point(5, 10)
    values = [5, 'hi', 2.5, 'there', pt, '7.2']

    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = (values[1]) * 5
    print(x)
    x = values[2:5]
    print(x)
    x = values[2:4] + [values[0]]
    print(x)
    x = [values[2]] + [values[0]] + [values[5]]
    print(x)
    x = values[0] + float(values[5]) + values[2]
    print(x)
    x = len(values)
    print(x)


def another_series():
    num = eval(input('enter number of terms: '))
    total = 0
    val = 0
    for i in range(num):
        val = val % 6
        val += 2
        total += val
        print(val, end=' ')
    print('\n', 'sum =', total)


def target():
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    center = Point(200, 200)

    shape = Circle(center, 200)
    shape.setOutline("black")
    shape.setFill("white")
    shape.draw(win)

    shape = Circle(center, 170)
    shape.setOutline("black")
    shape.setFill("black")
    shape.draw(win)

    shape = Circle(center, 140)
    shape.setOutline("black")
    shape.setFill("blue")
    shape.draw(win)

    shape = Circle(center, 110)
    shape.setOutline("black")
    shape.setFill("red")
    shape.draw(win)

    shape = Circle(center, 90)
    shape.setOutline("black")
    shape.setFill("yellow")
    shape.draw(win)

    msg = Text(Point(200, 200), 'Click again to close')
    msg.draw(win)
    win.getMouse()
    win.close()
