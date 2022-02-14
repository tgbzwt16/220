import graphics
from time import sleep
from graphics import *

def gift():
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)
    win.setBackground('white')

    line = Line(Point(-200, -200), Point(75, 75))
    line.setArrow('last')
    line.draw(win)

    inst_pt = Point(width / 2, height - 340)
    instructions = Text(inst_pt, "Happy Valentines Day!")
    instructions.setSize(30)
    instructions.setStyle('bold italic')
    instructions.setTextColor('red2')
    instructions.setFace('arial')
    instructions.draw(win)

    shape = Circle(Point(150, 150), 60)
    shape.setOutline("pink")
    shape.setFill("pink")
    shape.draw(win)

    shape1 = Circle(Point(250, 150), 60)
    shape1.setOutline("pink")
    shape1.setFill("pink")
    shape1.draw(win)

    shape2 = Polygon(Point(89, 150), Point(311, 150), Point(200, 300))
    shape2.setOutline("pink")
    shape2.setFill("pink")
    shape2.draw(win)
    for i in range(50):
        line.move(5,5)
        time.sleep(.2)

    msg = Text(Point(200, 350), 'Click to close')
    msg.draw(win)
    win.getMouse()
    win.close()


