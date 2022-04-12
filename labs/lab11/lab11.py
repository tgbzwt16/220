from lab10.door import Door
from lab10.button import Button
from graphics import *
import random


def door_game():
    width = 600
    height = 600
    win = GraphWin("three_door_game", width, height)
    win.setBackground('grey')

    button_shape = Rectangle(Point(300, 25), Point(450, 75))
    button_label = 'Quit'
    button = Button(button_shape, button_label)
    button.color_button('blue')
    button.draw(win)

    wins = Text(Point(115, 20), 'wins')
    wins.draw(win)
    win_shape = Rectangle(Point(75, 25), Point(150, 75))
    win_shape.setFill('white')
    win_shape.draw(win)

    loses = Text(Point(190, 20), 'losses')
    loses.draw(win)
    lose_shape = Rectangle(Point(150, 25), Point(225, 75))
    lose_shape.setFill('white')
    lose_shape.draw(win)

    door_shape = Rectangle(Point(100, 150), Point(200, 450))
    door_label = 'door1'
    door = Door(door_shape, door_label)
    door.color_door('light blue')
    door.draw(win)

    door2_shape = Rectangle(Point(250, 150), Point(350, 450))
    door2_label = 'door2'
    door2 = Door(door2_shape, door2_label)
    door2.color_door('light blue')
    door2.draw(win)

    door3_shape = Rectangle(Point(400, 150), Point(500, 450))
    door3_label = 'door3'
    door3 = Door(door3_shape, door3_label)
    door3.color_door('light blue')
    door3.draw(win)

    instruction = Text(Point(300, 500), "Click to guess which is the secret door")
    instruction.draw(win)

    words = ['door1', 'door2', 'door3']
    secret = ''
    x = random.randint(0, len(words) - 1)
    secret += words[x]

    msg = Text(Point(300, 125), 'I have a secret door')
    msg.draw(win)
    game_over = Text(Point(300, 500), 'Click again to play')
    points = Text(Point(115, 50), '1')
    pointsL = Text(Point(190, 50), '1')

    while button.is_clicked(win.getMouse()) is False:
        y = win.getMouse()
        if door.is_clicked(y) is True and door.get_label() == secret:
            door.open('green', 'door1')
            msg.undraw()
            notice = Text(Point(300, 125), 'you win!')
            notice.draw(win)
            points.draw(win)
            instruction.undraw()
            game_over.draw(win)
            break
        elif door.is_clicked(y) is True and door.get_label() != secret:
            msg.undraw()
            door.open('red', 'door2')
            notice2 = Text(Point(300, 125), 'sorry incorrect!')
            notice2.draw(win)
            pointsL.draw(win)
        elif door2.is_clicked(y) is True and door2.get_label() == secret:
            msg.undraw()
            door2.open('green', 'door2')
            notice = Text(Point(300, 125), 'you win!')
            notice.draw(win)
            points.draw(win)
            instruction.undraw()
            game_over.draw(win)
            break
        elif door2.is_clicked(y) is True and door2.get_label() != secret:
            msg.undraw()
            door2.open('red', 'door2')
            notice2 = Text(Point(300, 125), 'sorry incorrect!')
            notice2.draw(win)
            pointsL.draw(win)
        elif door3.is_clicked(y) is True and door3.get_label() == secret:
            msg.undraw()
            door3.open('green', 'door3')
            notice = Text(Point(300, 125), 'you win!')
            notice.draw(win)
            points.draw(win)
            instruction.undraw()
            game_over.draw(win)
            break
        elif door3.is_clicked(y) is True and door3.get_label() != secret:
            msg.undraw()
            door3.open('red', 'door2')
            notice2 = Text(Point(300, 125), 'sorry incorrect!')
            notice2.draw(win)
            pointsL.draw(win)
        elif button.is_clicked(y) is True:
            win.close()

    win.getMouse()
    return False


if __name__ == '__main__':
    door_game()
    while door_game() is False:
        door_game()

