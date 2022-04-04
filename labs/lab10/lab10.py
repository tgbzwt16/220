from graphics import *
from button import Button
from door import Door


def door_program():
    width = 400
    height = 400
    win = GraphWin("Test", width, height)
    win.setBackground('light gray')

    b_shape = Rectangle(Point(50, 40), Point(350, 90))
    label = 'Exit'
    button = Button(b_shape, label)
    button.color_button('light blue')
    button.draw(win)

    d_shape = Rectangle(Point(115, 105), Point(285, 365))
    label2 = 'Closed'
    door = Door(d_shape, label2)
    door.color_door('blue')
    door.draw(win)

    while button.is_clicked(win.getMouse()) is False:
        y = win.getMouse()
        if door.is_clicked(y) is True and door.get_label() == 'Closed':
            door.open('green', 'Open')
        elif door.is_clicked(y) is True and door.get_label() == 'Open':
            door.close('blue', 'Closed')
        elif button.is_clicked(y) is True:
            win.close()


if __name__ == '__main__':
    door_program()