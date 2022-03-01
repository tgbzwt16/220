from graphics import *


def encode_msg():
    width = 400
    height = 400
    win = GraphWin("Vigenere", width, height)
    win.setBackground('light gray')

    text_pt1 = Point(75, 100)
    text1 = Text(text_pt1, "Message to code: ")
    input_box1 = Entry(Point(250, 100), 30)
    input_box1.draw(win)
    text1.draw(win)
    text1.setTextColor("black")

    text_pt = Point(100, 150)
    text = Text(text_pt, "Enter Keyword: ")
    input_box = Entry(Point(250, 150), 20)
    input_box.draw(win)
    text.draw(win)
    text.setTextColor("black")

    button = Rectangle(Point(150, 200), Point(300, 250))
    text2 = Text(Point(225, 225), 'Encode')
    button.setFill('white')
    button.draw(win)
    text2.draw(win)

    win.getMouse()
    button.undraw()
    text2.undraw()

    msg = input_box1.getText()
    key = input_box.getText()
    msg = msg.upper().replace(' ', '')
    key = key.upper().replace(' ', '')

    encoded_str = ''
    for i in range(len(msg)):
        msg_ord = (ord(msg[i])) - 65
        key_ord = (ord(key[i % len(key)])) - 65
        total = (msg_ord + key_ord) % 58
        new_ord = total + 65
        encoded_chr = (chr(new_ord))
        encoded_str = encoded_str + encoded_chr

    text3 = Text(Point(215, 225), encoded_str)
    text3.draw(win)

    msg = Text(Point(200, 350), 'Click anywhere to close')
    msg.draw(win)
    win.getMouse()
    win.close()





