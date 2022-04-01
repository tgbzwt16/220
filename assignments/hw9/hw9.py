import random
from graphics import GraphWin, Text, Entry, Point, Circle, Line


def get_words(file_name):
    new_list = []
    file_open = open(file_name, 'r')
    file_read = file_open.readlines()
    for i in file_read:
        new_list += [i]
    return new_list


def get_random_word(words):
    string = ''
    x = random.randint(0, len(words)-1)
    string += words[x]
    return string.rstrip()


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    return False


def already_guessed(letter, guesses):
    if letter not in guesses:
        return False
    return True


def make_hidden_secret(secret_word, guesses):
    secret = ''
    for i in secret_word:
        if i in guesses:
            secret += i + ' '
        elif i not in guesses:
            i = '_'
            secret += i + ' '
    return secret.rstrip()


def won(guessed):
    k = '_'
    if k in guessed:
        return False
    return True


def play_graphics(secret_word):
    width = 400
    height = 400
    win = GraphWin("hangman", width, height)
    win.setBackground('light gray')

    line1 = Line(Point(200, 50), Point(200, 300))
    line1.draw(win)
    line2 = Line(Point(100, 50), Point(200, 50))
    line2.draw(win)
    line3 = Line(Point(100, 50), Point(100, 100))
    line3.draw(win)
    line4 = Line(Point(100, 300), Point(300, 300))
    line4.draw(win)

    guess_list = []
    k = len(secret_word)
    guess_string = ''

    x = 350
    y = 50

    while k > 0:
        text_pt1 = Point(120, 350)
        text1 = Text(text_pt1, "Guess a letter: ")
        input_box = Entry(Point(200, 350), 10)
        input_box.draw(win)
        text1.draw(win)
        text1.setTextColor("black")

        win.getMouse()

        notice = Text(Point(350, 30), 'already guessed:')
        notice.draw(win)
        letter = input_box.getText()
        guessed = Text(Point(x, y), letter)
        guessed.setTextColor('red')
        guessed.setSize(15)
        guessed.draw(win)
        y += 18

        guess = letter
        guess_string += guess
        result = make_hidden_secret(secret_word, guess_string)
        text = Text(Point(200, 325), result)
        text.draw(win)

        if already_guessed(guess, guess_list) is True:
            continue

        if won(result) is True:
            text1.undraw()
            input_box.undraw()
            winner = Text(Point(200, 25), 'winner!')
            winner.draw(win)
            break

        if letter_in_secret_word(guess, secret_word) is False:
            k -= 1

        if k == (len(secret_word) - 1):
            head = Circle(Point(100, 120), 20)
            head.draw(win)
            mouth = Circle(Point(100, 130), 5)
            mouth.draw(win)
            eye1 = Line(Point(89, 110), Point(94, 118))
            eye1.draw(win)
            eye2 = Line(Point(105, 110), Point(110, 118))
            eye2.draw(win)
            eye3 = Line(Point(94, 110), Point(89, 118))
            eye3.draw(win)
            eye4 = Line(Point(110, 110), Point(105, 118))
            eye4.draw(win)

        if k == (len(secret_word) - 2):
            body = Line(Point(100, 140), Point(100, 220))
            body.draw(win)

        if k == (len(secret_word) - 3):
            arm1 = Line(Point(100, 155), Point(50, 180))
            arm1.draw(win)

        if k == (len(secret_word) - 4):
            arm2 = Line(Point(100, 155), Point(150, 180))
            arm2.draw(win)

        if k == (len(secret_word) - 5):
            leg1 = Line(Point(100, 220), Point(40, 280))
            leg1.draw(win)

        if k == (len(secret_word) - 6):
            leg2 = Line(Point(100, 220), Point(160, 280))
            leg2.draw(win)

        if k == 0:
            text1.undraw()
            input_box.undraw()
            lose = Text(Point(200, 20), 'sorry, you did not guess the word.')
            loser = Text(Point(170, 40), 'the secret word was:')
            reveal = Text(Point(245, 40), secret_word)
            lose.draw(win)
            loser.draw(win)
            reveal.draw(win)
            break

        guess_list.append(guess)
        text1.undraw()
        input_box.undraw()

    msg = Text(Point(200, 350), 'Click anywhere to close')
    msg.draw(win)
    win.getMouse()
    win.close()


def play_command_line(secret_word):
    guess_list = []
    k = len(secret_word)
    guess_string = ''
    print('already guessed: ', guess_list)
    print('guesses remaining: ', k)
    result = make_hidden_secret(secret_word, guess_string)
    print(result)

    while k > 0:
        print('already guessed: ', guess_list)
        print('guesses remaining: ', k)
        guess = input('guess a letter: ')
        guess_string += guess
        result = make_hidden_secret(secret_word, guess_string)
        print(result)

        if already_guessed(guess, guess_list) is True:
            print('the letter has already been guessed, guess another letter')
            continue

        if won(result) is True:
            print('winner!')
            break

        if letter_in_secret_word(guess, secret_word) is False:
            k -= 1

        if k == 0:
            print('sorry, you did not guess the word.')
            print('the secret word was', secret_word)
            break

        guess_list.append(guess)


if __name__ == '__main__':
    word_list = get_words('words.txt')
    s_word = get_random_word(word_list)
    play_command_line(s_word)
    play_graphics(s_word)
