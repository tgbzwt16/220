import random


def find_and_remove_first(alist, value):
    if value not in alist:
        return None
    k = 0
    while k < len(alist):
        if value == alist[k]:
            alist.remove(alist[k])
            alist.insert(k, 'Thomas')
            break
        k += 1
    return alist


def good_input():
    while True:
        val = eval(input('Enter a value from 1-10: '))
        if val < 1 or val > 10:
            print('The value is not in the range of 1 to 10! Try again')
            continue
        else:
            return val


def num_digits():
    while True:
        val = int(input("Enter a positive number: "))
        if val < 1:
            break
        else:
            count = 0
            while val > 0:
                count = count + 1
                val = val // 10
            print(count)


def hi_lo_game():
    number = random.randint(2, 99)

    k = 1
    while k < 8:
        user = eval(input('Guess a number between 1 and 100: '))
        if user == number:
            winner = 'You win in' + ' ' + str(k) + ' ' + 'guess!'
            print(winner)
            break
        elif user < number:
            print('too low!')
        elif user > number:
            print('too high!')
        k += 1
    if k == 8:
        print('Sorry, you lose, the number was' + ' ' + str(number))


if __name__ == '__main__':
    x = ['12', 4, 'but', 12, 'but', 12, 12]
    print(find_and_remove_first(x, 12))
    print(find_and_remove_first(x, 1))
    print(good_input())
    print(num_digits())
    print(hi_lo_game())
