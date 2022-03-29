"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if board[position-1] == 'x' or board[position-1] == 'o':
        return False
    else:
        return True


def fill_spot(board, position, shape):
    shape = shape.strip().lower()
    board[position-1] = shape


def winning_game(board):
    if board[0] == board[1] == board[2]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[0] == board[4] == board[8]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True
    else:
        return False


def game_over(board):
    acc = 0
    for i in board:
        if i == 'x':
            acc += 1
        if i == 'o':
            acc += 1

    if acc == 9:
        return True
    else:
        return winning_game(board)


def get_winner(board):
    if winning_game(board):
        xCount = 0
        oCount = 0

        for position in board:
            if position == 'x':
                xCount += 1
            elif position == 'o':
                oCount += 1

        if xCount == oCount:
            return 'o'
        else:
            return 'x'

    else:
        return None


def play(board):
    while True:
        print_board(board)
        play1 = eval(input('enter a number from 1-9 to play X '))

        if is_legal(board, play1) is True:
            shape = 'x'
            fill_spot(board, play1, shape)
        else:
            print('the spot is already taken! choose another one')
            continue
        print_board(board)

        if winning_game(board) is True:
            winner = get_winner(board)
            print('winner: ', winner)
            break

        if game_over(board) is True:
            print('Draw')
            break

        play2 = eval(input('enter a number from 1-9 to play O '))

        if is_legal(board, play2) is True:
            shape = 'o'
            fill_spot(board, play2, shape)
        else:
            # For some reason the code to make the user re-enter input
            # didn't work with the O player, but it worked
            # with the X player.
            print('the spot is already taken! choose another one')
            continue
        print_board(board)

        if winning_game(board) is True:
            winner = get_winner(board)
            print('winner: ', winner)
            break

        if game_over(board) is True:
            print('Draw')
            break


if __name__ == '__main__':
    x = build_board()
    play(x)
    while True:
        if game_over(x) is True:
            play_again = input('Do you want to play again? (y or n) ')
            if play_again == 'y' or play_again == 'Y':
                y = build_board()
                play(y)
            else:
                break
